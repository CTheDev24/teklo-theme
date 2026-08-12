[CmdletBinding()]
param([ValidateRange(1,3)][int]$MaxIterations=3,[string]$CodexCommand="codex",[string]$ShopifyCommand="shopify",[switch]$ValidateOnly,[switch]$ResumeAfterImplementation)
$ErrorActionPreference="Stop"
$root=(Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$schema=Join-Path $PSScriptRoot "review.schema.json"; $handoff=Join-Path $PSScriptRoot "last-review.json"
$implementer=Join-Path $PSScriptRoot "prompts\implementer.md"; $reviewer=Join-Path $PSScriptRoot "prompts\reviewer.md"
$check=Join-Path $PSScriptRoot "theme-check.txt"
$capture=Join-Path $PSScriptRoot "capture-fixture.ps1"
$desktop=Join-Path $PSScriptRoot "evidence\current\desktop-1440x1000.png"; $mobile=Join-Path $PSScriptRoot "evidence\current\mobile-390x844.png"
function Assert-FeatureBranch { $b=(& git -C $root branch --show-current).Trim(); if($LASTEXITCODE -ne 0-or [string]::IsNullOrWhiteSpace($b)){throw "A named Git branch is required."}; if($b -in @("main","master")-or $b -notmatch '^(feature/|codex/feature/)'){throw "Refusing branch '$b'; use feature/ or codex/feature/."} }
function Get-PngSize([string]$p){ if(!(Test-Path -LiteralPath $p -PathType Leaf)){throw "Missing evidence: $p"}; $x=[IO.File]::ReadAllBytes($p); if($x.Length-lt 24-or $x[0]-ne 137-or $x[1]-ne 80-or $x[2]-ne 78-or $x[3]-ne 71){throw "Unreadable PNG: $p"}; @([Net.IPAddress]::NetworkToHostOrder([BitConverter]::ToInt32($x,16)),[Net.IPAddress]::NetworkToHostOrder([BitConverter]::ToInt32($x,20))) }
function Assert-Evidence([datetime]$since){ foreach($t in @(@($desktop,1440,1000),@($mobile,390,844))){$f=Get-Item -LiteralPath $t[0] -ErrorAction Stop;if($f.LastWriteTimeUtc-lt $since.ToUniversalTime()){throw "Stale evidence: $($t[0])"};$s=Get-PngSize $t[0];if($s[0]-ne $t[1]-or $s[1]-ne $t[2]){throw "Wrong dimensions: $($t[0]) is $($s[0])x$($s[1])"}} }
function Read-Review { $r=Get-Content -Raw -LiteralPath $handoff|ConvertFrom-Json;if($r.verdict-notin @("accepted","revise","human_review")){throw "Invalid verdict"};if($r.evidence.source-notin @("local_fixture","shopify_preview")){throw "Invalid evidence source"};if($r.verdict-eq "accepted"-and @($r.findings).Count-ne 0){throw "Accepted cannot have findings"};if($r.verdict-ne "human_review"-and -not [string]::IsNullOrEmpty($r.human_decision)){throw "Only human_review may request a human decision"};if($r.verdict-eq "revise"-and @($r.findings).Count-eq 0){throw "Revise needs findings"};if($r.verdict-eq "human_review"-and [string]::IsNullOrWhiteSpace($r.human_decision)){throw "Human decision missing"};$r }
Assert-FeatureBranch
foreach($p in @($schema,$handoff,$implementer,$reviewer,$capture)){if(!(Test-Path -LiteralPath $p -PathType Leaf)){throw "Missing workflow file: $p"}}
$null=Get-Content -Raw -LiteralPath $schema|ConvertFrom-Json;$null=Read-Review
if($ValidateOnly){Write-Host "Workflow validation passed; no Codex or Shopify process was started.";exit 0}
foreach($c in @($CodexCommand,$ShopifyCommand)){if(!(Get-Command $c -ErrorAction SilentlyContinue)){throw "Required command not found: $c"}}
for($i=1;$i-le $MaxIterations;$i++){
 Assert-FeatureBranch;$started=Get-Date
 if($ResumeAfterImplementation-and $i-eq 1){Write-Host "Iteration $i resuming after completed implementation"}else{
  Write-Host "Iteration $i implementation"
  Get-Content -Raw -LiteralPath $implementer|& $CodexCommand exec --sandbox workspace-write -C $root -
  if($LASTEXITCODE-ne 0){throw "Implementation failed"}
 }
 & powershell.exe -NoProfile -ExecutionPolicy Bypass -File $capture;if($LASTEXITCODE-ne 0){throw "Fixture capture failed"}
 Assert-Evidence $started;Assert-FeatureBranch;Write-Host "Iteration $i theme check"
 $previousErrorPreference=$ErrorActionPreference
 $ErrorActionPreference="Continue"
 & $ShopifyCommand theme check --path $root --no-color 2>&1|Tee-Object -FilePath $check
 $themeCheckExit=$LASTEXITCODE
 $ErrorActionPreference=$previousErrorPreference
 if($themeCheckExit-ne 0){
  $themeCheckText=Get-Content -Raw -LiteralPath $check
  $knownWindowsShutdownBug=$themeCheckText -match 'Theme Check Summary\.' -and $themeCheckText -match 'UV_HANDLE_CLOSING' -and $themeCheckText -notmatch '\[error\]' -and $themeCheckText -notmatch '\d+ errors\.'
  if(!$knownWindowsShutdownBug){throw "Theme Check failed; see $check"}
  Write-Warning "Shopify CLI hit its known Windows shutdown assertion after a complete error-free summary; continuing with the captured report."
}
 Assert-FeatureBranch;Write-Host "Iteration $i read-only review"
 Get-Content -Raw -LiteralPath $reviewer|& $CodexCommand exec --sandbox read-only -C $root --output-schema $schema --output-last-message $handoff -;if($LASTEXITCODE-ne 0){throw "Review failed"}
 $r=Read-Review;if($r.verdict-eq "accepted"-and $r.evidence.source-ne "shopify_preview"){throw "Local fixture evidence cannot be accepted"};if($r.verdict-eq "accepted"){Write-Host "Accepted after iteration $i";exit 0};if($r.verdict-eq "human_review"){Write-Host "Human review: $($r.human_decision)";exit 2};if($i-eq $MaxIterations){Write-Host "Iteration limit reached";exit 3}
}
