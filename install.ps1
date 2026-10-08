<#
.SYNOPSIS
    Claude Platform Master Skill - Windows PowerShell Installer
.DESCRIPTION
    Installs the claude-platform-master skill into Claude Code or Google Antigravity.
.PARAMETER Global
    Install globally for all user projects (default).
.PARAMETER Project
    Install into the current repository project directory.
.PARAMETER Claude
    Target Claude Code explicitly.
.PARAMETER Antigravity
    Target Google Antigravity explicitly.
.PARAMETER DryRun
    Simulate installation without modifying files.
.PARAMETER Uninstall
    Remove the installed skill.
#>

[CmdletBinding()]
param (
    [switch]$Global = $true,
    [switch]$Project,
    [switch]$Claude,
    [switch]$Antigravity,
    [switch]$DryRun,
    [switch]$Uninstall
)

$RepoOwner = "joardo"
$RepoName = "claude-code-knowledge-vault"
$Branch = "main"
$RawBaseUrl = "https://raw.githubusercontent.com/$RepoOwner/$RepoName/$Branch"
$SkillName = "claude-platform-master"

Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host "  Claude Platform Master Skill Installer (Windows)" -ForegroundColor Cyan
Write-Host "  Expert Tool Selection Architect for Claude Code" -ForegroundColor Cyan
Write-Host "==========================================================" -ForegroundColor Cyan
Write-Host ""

$TargetEnv = "claude"
if ($Antigravity) {
    $TargetEnv = "antigravity"
} elseif (-not $Claude) {
    # Auto-detect
    $GeminiPath = Join-Path $HOME ".gemini"
    $ClaudePath = Join-Path $HOME ".claude"
    if ((Test-Path $GeminiPath) -and -not (Test-Path $ClaudePath)) {
        $TargetEnv = "antigravity"
    }
}

$TargetScope = if ($Project) { "project" } else { "global" }

if ($TargetEnv -eq "claude") {
    if ($TargetScope -eq "global") {
        $DestDir = Join-Path $HOME ".claude\skills\$SkillName"
    } else {
        $DestDir = Join-Path (Get-Location) ".claude\skills\$SkillName"
    }
} else {
    if ($TargetScope -eq "global") {
        $DestDir = Join-Path $HOME ".gemini\config\skills\$SkillName"
    } else {
        $DestDir = Join-Path (Get-Location) ".agents\skills\$SkillName"
    }
}

if ($DryRun) {
    Write-Host "[DRY-RUN] Target Environment : $TargetEnv" -ForegroundColor Yellow
    Write-Host "[DRY-RUN] Target Scope       : $TargetScope" -ForegroundColor Yellow
    Write-Host "[DRY-RUN] Destination Path   : $DestDir" -ForegroundColor Yellow
    Write-Host "[DRY-RUN] Dry run complete. No files written." -ForegroundColor Green
    exit 0
}

if ($Uninstall) {
    if (Test-Path $DestDir) {
        Remove-Item -Recurse -Force $DestDir
        Write-Host "Successfully removed skill from: $DestDir" -ForegroundColor Green
    } else {
        Write-Host "Skill not found at: $DestDir" -ForegroundColor Yellow
    }
    exit 0
}

Write-Host "Target Environment : $TargetEnv" -ForegroundColor Cyan
Write-Host "Target Scope       : $TargetScope" -ForegroundColor Cyan
Write-Host "Destination Path   : $DestDir" -ForegroundColor Cyan
Write-Host ""

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$LocalSkillDir = Join-Path $ScriptDir "skills\$SkillName"

$RefDir = Join-Path $DestDir "references"
if (-not (Test-Path $RefDir)) {
    New-Item -ItemType Directory -Path $RefDir -Force | Out-Null
}

if ((Test-Path $LocalSkillDir) -and (Test-Path (Join-Path $LocalSkillDir "SKILL.md"))) {
    Write-Host "Installing from local source: $LocalSkillDir..."
    Copy-Item -Path "$LocalSkillDir\*" -Destination $DestDir -Recurse -Force
} else {
    Write-Host "Installing via remote download from $RawBaseUrl..."
    Invoke-WebRequest -Uri "$RawBaseUrl/skills/$SkillName/SKILL.md" -OutFile (Join-Path $DestDir "SKILL.md")
    Invoke-WebRequest -Uri "$RawBaseUrl/skills/$SkillName/references/capability_cheat_sheet.md" -OutFile (Join-Path $RefDir "capability_cheat_sheet.md")
    Invoke-WebRequest -Uri "$RawBaseUrl/skills/$SkillName/references/consultation_examples.md" -OutFile (Join-Path $RefDir "consultation_examples.md")
}

Write-Host ""
Write-Host "Installation Successful!" -ForegroundColor Green
Write-Host "Skill installed to: $DestDir"
Write-Host ""
Write-Host "Next Steps:" -ForegroundColor White
if ($TargetEnv -eq "claude") {
    Write-Host "  1. Run Claude Code: claude" -ForegroundColor Green
    Write-Host "  2. Type slash command: /claude-platform-master" -ForegroundColor Green
} else {
    Write-Host "  1. Launch Antigravity: agy" -ForegroundColor Green
    Write-Host "  2. The skill is now active for prompt consultation." -ForegroundColor Green
}
