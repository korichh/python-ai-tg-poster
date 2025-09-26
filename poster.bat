@echo off
cd /d %~dp0

echo [INFO] Starting application setup...
echo [INFO] Current directory: %CD%

REM Check if Python is installed
echo [INFO] Checking Python installation...

python --version >nul 2>&1

if errorlevel 1 (
    echo [ERROR] Python is not installed
    pause
    exit /b 1
)
echo [INFO] Python is available

REM Ensure virtual environment exists
echo [INFO] Checking virtual environment...

if not exist ".venv\Scripts\activate.bat" (
    echo [INFO] Virtual environment not found, creating...
    
    python -m venv .venv
    
    if errorlevel 1 (
        echo [ERROR] Failed to create virtual environment
        pause
        exit /b 1
    )
    echo [INFO] Virtual environment created
) else (
    echo [INFO] Virtual environment already exists
)

REM Activate virtual environment
echo [INFO] Activating virtual environment...

call .venv\Scripts\activate.bat

echo [INFO] Virtual environment activated

REM Install dependencies if requirements.txt exists
echo [INFO] Checking for dependencies...

if exist "requirements.txt" (
    echo [INFO] Found requirements.txt, installing dependencies...
    
    pip install -r requirements.txt
    
    if errorlevel 1 (
        echo [WARNING] Some dependencies have failed to install
    ) else (
        echo [INFO] Dependencies installed successfully
    )
) else (
    echo [INFO] No requirements.txt found, skipping dependency installation
)

REM Check if Python script exists
echo [INFO] Checking for Python script...

if not exist "src\index.py" (
    echo [ERROR] Python script not found at src\index.py
    pause
    exit /b 1
)

echo [INFO] Python script found

REM Run the Python script
echo [INFO] Starting application...

echo ========================================

python src\index.py

echo ========================================

echo [INFO] Application finished

pause
