"""Audita la integridad y busca números de identidad etiquetados en un PPTX."""
from pathlib import Path
from zipfile import ZipFile
from xml.etree import ElementTree
import re, sys

source=Path(sys.argv[1]) if len(sys.argv)>1 else Path('entregables/estadistica_ii/presentacion-mobile-statics.pptx')
pattern=re.compile(r'(?i)\b(?:c\.?\s*i\.?|c[eé]dula(?:\s+de\s+identidad)?)\s*[:#-]?\s*\d[\d.\s-]{4,}\d')
with ZipFile(source) as archive:
    corrupt=archive.testzip()
    names=archive.namelist()
    slides=sorted((name for name in names if re.fullmatch(r'ppt/slides/slide\d+\.xml',name)),key=lambda n:int(re.search(r'slide(\d+)',n).group(1)))
    findings=[]
    scanned=0
    for name in names:
        if not name.startswith(('ppt/slides/','ppt/notesSlides/')) or not name.endswith('.xml'):
            continue
        root=ElementTree.fromstring(archive.read(name))
        content=' '.join(node.text or '' for node in root.iter() if node.tag.endswith('}t'))
        matches=list(pattern.finditer(content))
        if matches: findings.append((name,len(matches)))
        scanned+=1
result={'file_bytes':source.stat().st_size,'zip_integrity':'pass' if corrupt is None else 'fail','slides':len(slides),'slide_and_notes_xml_scanned':scanned,'labelled_identity_matches':sum(n for _,n in findings),'affected_xml_files':[n for n,_ in findings]}
print(result)
if corrupt or len(slides)!=33 or findings: raise SystemExit(1)
