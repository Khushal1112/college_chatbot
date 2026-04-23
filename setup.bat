@echo off
REM College Chatbot - Quick Setup Script for Windows
REM This script automates the setup process for the chatbot

echo.
echo ========================================
echo   College Chatbot - Setup Script
echo ========================================
echo.

REM Check Python version
echo [1/6] Checking Python version...
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Python is not installed. Please install Python 3.8 or higher.
    pause
    exit /b 1
)
python --version
echo [OK] Python found
echo.

REM Create virtual environment
echo [2/6] Creating virtual environment...
if exist "venv" (
    echo [WARNING] Virtual environment already exists. Skipping...
) else (
    python -m venv venv
    echo [OK] Virtual environment created
)
echo.

REM Activate virtual environment
echo [3/6] Activating virtual environment...
call venv\Scripts\activate.bat
echo [OK] Virtual environment activated
echo.

REM Upgrade pip
echo [4/6] Upgrading pip...
python -m pip install --upgrade pip >nul 2>&1
echo [OK] pip upgraded
echo.

REM Install dependencies
echo [5/6] Installing dependencies...
pip install -r requirements.txt
if errorlevel 1 (
    echo [ERROR] Failed to install dependencies
    pause
    exit /b 1
)
echo [OK] Dependencies installed successfully
echo.

REM Run tests
echo [6/6] Running tests...
python test_chatbot.py
if errorlevel 1 (
    echo [WARNING] Some tests failed, but setup is complete
) else (
    echo [OK] All tests passed
)
echo.

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo [BONUS] Creating .env file...
    (
        echo # Flask Configuration
        echo SECRET_KEY=college-chatbot-secret-2024-change-this-in-production
        echo FLASK_ENV=development
        echo FLASK_DEBUG=True
        echo.
        echo # Server Configuration
        echo HOST=0.0.0.0
        echo PORT=5000
        echo.
        echo # Chatbot Configuration
        echo INTENTS_PATH=Dataset/intents.json
        echo CONFIDENCE_THRESHOLD=0.2
    ) > .env
    echo [OK] .env file created
) else (
    echo [INFO] .env file already exists. Skipping...
)
echo.

REM Display success message
echo ========================================
echo   Setup Complete!
echo ========================================
echo.
echo To start the application:
echo   1. Activate virtual environment: venv\Scripts\activate
echo   2. Run the app: python app.py
echo   3. Open browser: http://localhost:5000
echo.
echo For more information, see README.md
echo.
pause
