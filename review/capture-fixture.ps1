[CmdletBinding()]param([string]$ChromePath)
$ErrorActionPreference="Stop"
$root=(Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$fixture=(Resolve-Path (Join-Path $PSScriptRoot "fixture\index.html")).Path
if(!$ChromePath){$ChromePath=@("$env:ProgramFiles\Google\Chrome\Application\chrome.exe","${env:ProgramFiles(x86)}\Google\Chrome\Application\chrome.exe","$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe")|Where-Object{Test-Path -LiteralPath $_}|Select-Object -First 1}
if(!$ChromePath-or !(Test-Path -LiteralPath $ChromePath)){throw "Chrome not found. Pass -ChromePath."}
$out=Join-Path $PSScriptRoot "evidence\current";[IO.Directory]::CreateDirectory($out)|Out-Null
$profile=Join-Path ([IO.Path]::GetTempPath()) ("teklo-fixture-"+[guid]::NewGuid().ToString("N"));[IO.Directory]::CreateDirectory($profile)|Out-Null
$url=([Uri]$fixture).AbsoluteUri
$desktopFixture=Join-Path (Split-Path $fixture) "capture-desktop.html"
$desktopMarkup=[IO.File]::ReadAllText($fixture).Replace('<html lang="en">','<html lang="en" class="capture-desktop">')
[IO.File]::WriteAllText($desktopFixture,$desktopMarkup,(New-Object Text.UTF8Encoding($false)))
$desktopUrl=([Uri]$desktopFixture).AbsoluteUri
$mobileFixture=Join-Path (Split-Path $fixture) "capture-mobile.html"
$mobileMarkup=[IO.File]::ReadAllText($fixture).Replace('<html lang="en">','<html lang="en" class="capture-mobile">')
[IO.File]::WriteAllText($mobileFixture,$mobileMarkup,(New-Object Text.UTF8Encoding($false)))
$mobileUrl=([Uri]$mobileFixture).AbsoluteUri
try{
 foreach($shot in @(@("desktop-1440x1000.png",1440,1000),@("mobile-390x844.png",390,844))){
  $shotProfile=$profile+"-"+$shot[1];[IO.Directory]::CreateDirectory($shotProfile)|Out-Null
  $dest=Join-Path $out $shot[0];if(Test-Path -LiteralPath $dest){Remove-Item -LiteralPath $dest -Force}
  $captureUrl=if($shot[1]-eq 390){$mobileUrl}else{$desktopUrl}
  $args=@("--headless=new","--disable-gpu","--hide-scrollbars","--no-first-run","--force-device-scale-factor=1","--user-data-dir=$shotProfile","--window-size=$($shot[1]),$($shot[2])","--screenshot=$dest",$captureUrl)
  $proc=Start-Process -FilePath $ChromePath -ArgumentList $args -PassThru -WindowStyle Hidden
  $deadline=(Get-Date).AddSeconds(20);while((Get-Date)-lt $deadline-and (!(Test-Path -LiteralPath $dest)-or (Get-Item -LiteralPath $dest).Length-eq 0)){Start-Sleep -Milliseconds 200}
  if(!$proc.HasExited){$oldPreference=$ErrorActionPreference;$ErrorActionPreference="SilentlyContinue";& taskkill.exe /PID $proc.Id /T /F *> $null;$ErrorActionPreference=$oldPreference}
  if(!(Test-Path -LiteralPath $dest)-or (Get-Item -LiteralPath $dest).Length-eq 0){throw "Capture failed: $($shot[0])"}
 }
}finally{if(Test-Path -LiteralPath $profile){Remove-Item -LiteralPath $profile -Recurse -Force -ErrorAction SilentlyContinue};if(Test-Path -LiteralPath $desktopFixture){Remove-Item -LiteralPath $desktopFixture -Force -ErrorAction SilentlyContinue};if(Test-Path -LiteralPath $mobileFixture){Remove-Item -LiteralPath $mobileFixture -Force -ErrorAction SilentlyContinue}}
Write-Host "Captured local fixture evidence. This evidence cannot establish Shopify acceptance."