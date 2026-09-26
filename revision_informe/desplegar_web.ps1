$ErrorActionPreference='Stop'
$repoRoot=Split-Path $PSScriptRoot -Parent
$siteRoot=Join-Path $repoRoot 'site'
$gitDir=Join-Path $repoRoot '.git'
$tempRoot=Join-Path $repoRoot 'tmp'
New-Item -ItemType Directory -Force -Path $tempRoot | Out-Null
$indexFile=Join-Path $tempRoot ('pages-index-'+[guid]::NewGuid().ToString('N'))
$oldIndex=$env:GIT_INDEX_FILE
function Invoke-SiteGit {
 param([Parameter(ValueFromRemainingArguments=$true)][string[]]$GitArgs)
 $result=& git --git-dir=$gitDir --work-tree=$siteRoot -C $siteRoot @GitArgs
 if($LASTEXITCODE -ne 0){throw "Git failed: $($GitArgs[0])"}
 return $result
}
try {
 $remoteRef=Invoke-SiteGit ls-remote origin refs/heads/gh-pages
 $parent=$null
 if($remoteRef){
  Invoke-SiteGit fetch origin gh-pages | Out-Null
  $parent=Invoke-SiteGit rev-parse FETCH_HEAD
 }
 $env:GIT_INDEX_FILE=$indexFile
 Invoke-SiteGit read-tree --empty
 Invoke-SiteGit add --all -- .
 $tree=Invoke-SiteGit write-tree
 if($parent){$commit=Invoke-SiteGit -GitArgs @('commit-tree',$tree,'-p',$parent,'-m','feat: publish reviewed Mobile-Statics explorer')}
 else{$commit=Invoke-SiteGit -GitArgs @('commit-tree',$tree,'-m','feat: publish reviewed Mobile-Statics explorer')}
 Invoke-SiteGit update-ref refs/heads/gh-pages $commit
 Invoke-SiteGit push origin refs/heads/gh-pages:refs/heads/gh-pages
 Write-Output "Published commit: $commit"
} finally {
 $env:GIT_INDEX_FILE=$oldIndex
 if(Test-Path -LiteralPath $indexFile){Remove-Item -LiteralPath $indexFile}
}
