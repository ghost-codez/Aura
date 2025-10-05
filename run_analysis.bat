@echo off
REM Meeting Insights Engine - One-Click Runner
REM This batch file runs the analysis with minimal user interaction

echo.
echo ========================================
echo  Meeting Insights Engine - Quick Run
echo ========================================
echo.

REM Change to the script directory
cd /d "%~dp0"

REM Check if Python is available
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python and try again
    pause
    exit /b 1
)

REM Run the analysis
echo Running meeting analysis...
echo.
python process_meeting.py

echo.
echo ========================================
echo Analysis complete! 
echo ========================================
echo.
echo Press any key to exit...
pause >nul