@echo off

@rem git pull

cd /d "%~dp0"

IF NOT EXIST "venv" (
    python -m pip install virtualenv
    echo "creating venv dir..."
    python -m venv venv
    echo "install all requirements..."
    venv\Scripts\python.exe -m pip install -r requirements.txt
)

venv\Scripts\python.exe durak\bot.py

pause