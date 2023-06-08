@echo off

cd /d "%~dp0"

IF EXIST "venv" (
    venv\Scripts\python.exe durak\bot.py
) ELSE (
    python -m pip install virtualenv
    python -m venv venv
    echo "please wait"
    venv\Scripts\python.exe -m pip install -r requirements.txt
)

venv\Scripts\python.exe durak\bot.py

pause