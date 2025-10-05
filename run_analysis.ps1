# Meeting Insights Engine - PowerShell Runner
# Advanced automation script with error handling and logging

param(
    [string]$TranscriptPath = "",
    [switch]$Silent = $false,
    [switch]$OpenOutput = $false
)

# Set execution policy for current user if needed
if ((Get-ExecutionPolicy -Scope CurrentUser) -eq "Restricted") {
    Write-Host "Setting execution policy for PowerShell scripts..." -ForegroundColor Yellow
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser -Force
}

# Change to script directory
Set-Location $PSScriptRoot

# Function to write colored output
function Write-ColorOutput($ForegroundColor) {
    $fc = $host.UI.RawUI.ForegroundColor
    $host.UI.RawUI.ForegroundColor = $ForegroundColor
    if ($args) {
        Write-Output $args
    } else {
        $input | Write-Output
    }
    $host.UI.RawUI.ForegroundColor = $fc
}

if (-not $Silent) {
    Write-ColorOutput Green @"

========================================
 Meeting Insights Engine - Quick Run
========================================

"@
}

# Check if Python is available
try {
    $pythonVersion = python --version 2>&1
    if ($LASTEXITCODE -ne 0) {
        throw "Python not found"
    }
    if (-not $Silent) {
        Write-Host "✅ Python detected: $pythonVersion" -ForegroundColor Green
    }
} catch {
    Write-ColorOutput Red "❌ ERROR: Python is not installed or not in PATH"
    Write-Host "Please install Python from https://python.org and try again"
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if specific transcript file was provided
if ($TranscriptPath -and (Test-Path $TranscriptPath)) {
    # Copy the specified file to the working directory temporarily
    $fileName = Split-Path $TranscriptPath -Leaf
    Copy-Item $TranscriptPath $fileName -Force
    if (-not $Silent) {
        Write-Host "📁 Using specified transcript: $TranscriptPath" -ForegroundColor Cyan
    }
}

# Run the analysis
if (-not $Silent) {
    Write-Host "🚀 Running meeting analysis..." -ForegroundColor Green
    Write-Host ""
}

try {
    # Run Python script and capture output
    $output = python process_meeting.py 2>&1
    
    if ($LASTEXITCODE -eq 0) {
        # Display the output
        $output | Write-Host
        
        if (-not $Silent) {
            Write-ColorOutput Green @"

========================================
✅ Analysis Complete!
========================================

"@
        }
        
        # Optionally open output file if created
        if ($OpenOutput -and (Test-Path "meeting_analysis_report.txt")) {
            Start-Process "meeting_analysis_report.txt"
        }
        
    } else {
        Write-ColorOutput Red "❌ Error occurred during analysis:"
        $output | Write-Host -ForegroundColor Red
        exit 1
    }
    
} catch {
    Write-ColorOutput Red "❌ Unexpected error: $_"
    exit 1
}

# Clean up temporary files if we copied them
if ($TranscriptPath -and $fileName -and $fileName -ne "sample_transcript.txt") {
    Remove-Item $fileName -Force -ErrorAction SilentlyContinue
}

if (-not $Silent) {
    Write-Host "Press any key to exit..." -NoNewline
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
}