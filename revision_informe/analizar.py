"""Revisión reproducible; no modifica los CSV ni el cuaderno históricos."""
from pathlib import Path
import json, hashlib, sys
import numpy as np
import pandas as pd
import scipy
from scipy import stats
import statsmodels.api as sm
from statsmodels.stats.diagnostic import het_breuschpagan, linear_reset
from statsmodels.stats.stattools import durbin_watson

ROOT = Path(__file__).resolve().parents[1]
OUT = Path(__file__).resolve().parent
raw = pd.read_csv(ROOT/'mobiles.csv')
clean = pd.read_csv(ROOT/'telefono_Act.csv')
d = clean[['Nombre','GHz_Procesador','Precio($)']].rename(columns={'GHz_Procesador':'x','Precio($)':'y'}).replace([np.inf,-np.inf],np.nan).dropna(subset=['x','y'])
x,y = d.x,d.y
n=len(d)
fit=lambda z: sm.OLS(z.y, sm.add_constant(z.x)).fit()
m=fit(d)
rob=m.get_robustcov_results(cov_type='HC3',use_t=True)
sxx=float(((x-x.mean())**2).sum()); syy=float(((y-y.mean())**2).sum()); sxy=float(((x-x.mean())*(y-y.mean())).sum())
cov=sxy/(n-1); r=float(x.corr(y))
assert np.isclose(cov/float(x.var(ddof=1)),m.params.x)
assert np.isclose(cov/(x.std()*y.std()),r)
assert np.isclose(r*r,m.rsquared)
assert np.isclose(m.ess+m.ssr,m.centered_tss)
assert np.isclose(np.cov(x,y,ddof=1)[0,1],cov)
independent=stats.linregress(x,y)
assert np.allclose([independent.slope,independent.intercept],[m.params.x,m.params['const']])
influence=m.get_influence(); cook=influence.cooks_distance[0]
ix=int(np.argmax(cook)); threshold=4/n
dedup=clean.drop_duplicates()[['Nombre','GHz_Procesador','Precio($)']].rename(columns={'GHz_Procesador':'x','Precio($)':'y'}).dropna(subset=['x','y'])
scenarios={'Historica':d,'Sin duplicado exacto':dedup,'Sin mayor Cook':d.drop(d.index[ix]),'Sin Cook mayor que 4/n':d.loc[cook<=threshold]}
sens=[]
for name,z in scenarios.items():
 f=fit(z);sens.append({'escenario':name,'n':len(z),'intercepto':float(f.params['const']),'pendiente':float(f.params.x),'r2':float(f.rsquared)})
raw_nonnull=raw.dropna()
pred=m.get_prediction(np.array([[1,2.5],[1,4.5]])).summary_frame(alpha=.05)
for row,x0 in enumerate([2.5,4.5]):
 center=m.params['const']+m.params.x*x0
 h0=1/n+(x0-x.mean())**2/sxx
 tc=stats.t.ppf(.975,n-2)
 delta_mean=tc*np.sqrt(m.mse_resid*h0)
 delta_obs=tc*np.sqrt(m.mse_resid*(1+h0))
 assert np.allclose(pred.iloc[row][['mean_ci_lower','mean_ci_upper','obs_ci_lower','obs_ci_upper']],
                    [center-delta_mean,center+delta_mean,center-delta_obs,center+delta_obs])
bp=het_breuschpagan(m.resid,m.model.exog,robust=True)
sw=stats.shapiro(m.resid)
reset=linear_reset(m,power=2,use_f=True,cov_type='HC3')
join=raw_nonnull.reset_index(drop=True)
inr=pd.to_numeric(join.price.str.replace('₹','',regex=False).str.replace(',','',regex=False),errors='coerce')
matches=np.isclose(clean['Precio($)'],inr*.012)
ghz_rebuilt=pd.to_numeric(join.processor.str.split(',').str[2].str.strip().str.split().str[0],errors='coerce')
ghz_matches=np.isclose(ghz_rebuilt,clean.GHz_Procesador,equal_nan=True)
assert matches.all() and ghz_matches.all()
result={'n':n,'raw_n':len(raw),'clean_n':len(clean),'raw_dropna_n':len(raw_nonnull),'same_names_after_dropna':raw_nonnull.mobile_name.tolist()==clean.Nombre.tolist(),'missing':clean.isna().sum().to_dict(),'raw_missing':raw.isna().sum().to_dict(),'duplicates_raw':int(raw.duplicated().sum()),'duplicates_clean':int(clean.duplicated().sum()),'duplicate_names':clean.loc[clean.duplicated(keep=False),'Nombre'].tolist(),'conversion_matches':int(matches.sum()),'conversion_join_rows':len(join),'mx':float(x.mean()),'my':float(y.mean()),'sx':float(x.std()),'sy':float(y.std()),'sxx':sxx,'syy':syy,'sxy':sxy,'covariance':cov,'r':r,'r2':float(m.rsquared),'adj_r2':float(m.rsquared_adj),'params':m.params.to_dict(),'se':m.bse.to_dict(),'t':m.tvalues.to_dict(),'p':m.pvalues.to_dict(),'ci':m.conf_int().values.tolist(),'hc3_se':rob.bse.tolist(),'hc3_ci':rob.conf_int().tolist(),'hc3_p':rob.pvalues.tolist(),'SSR_explained':float(m.ess),'SSE':float(m.ssr),'MSE':float(m.mse_resid),'s':float(np.sqrt(m.mse_resid)),'f':float(m.fvalue),'f_p':float(m.f_pvalue),'tcrit':float(stats.t.ppf(.975,n-2)),'predictions':pred.to_dict('records'),'shapiro':{'W':float(sw.statistic),'p':float(sw.pvalue)},'bp':{'LM':float(bp[0]),'p':float(bp[1])},'reset':{'F':float(reset.fvalue),'p':float(reset.pvalue)},'dw':float(durbin_watson(m.resid)),'cook_threshold':threshold,'cook_flagged':int((cook>threshold).sum()),'max_cook':{'name':d.iloc[ix].Nombre,'csv_row':int(d.index[ix])+2,'x':float(x.iloc[ix]),'y':float(y.iloc[ix]),'D':float(cook[ix])},'sensitivity':sens,'descriptive':d[['x','y']].describe().to_dict(),'hashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['mobiles.csv','telefono_Act.csv','app.ipynb']}}
result['ghz_rebuilt_matches']=int(ghz_matches.sum())
result['python_version']=sys.version.split()[0]
result['versions']={'numpy':np.__version__,'pandas':pd.__version__,'scipy':scipy.__version__,'statsmodels':sm.__version__}
result['comprobaciones']={'seleccion_historica':bool(result['same_names_after_dropna']),
 'precios_y_frecuencias_reconstruidos':bool(matches.all() and ghz_matches.all()),
 'covarianza_numpy':True,'regresion_scipy':True,'identidades_cov_r_pendiente_R2_ANOVA':True,
 'intervalos_formula_independiente':True}
(OUT/'resultados.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
d.assign(ajuste=m.fittedvalues,residuo=m.resid,cook=cook,fila_csv=d.index+2).to_csv(OUT/'pares_y_diagnosticos.csv',index=False)
print(json.dumps(result,ensure_ascii=False,indent=2))
