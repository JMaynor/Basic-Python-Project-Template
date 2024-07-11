@echo off

REM Change directory to the script's location
cd /d %~dp0

REM Check if venv exists, if not create it
if not exist ".venv" (
  python -m venv .venv
)

REM Activate the virtual environment
call .venv\Scripts\activate.bat

REM Install dependencies from requirements.txt
pip install -r requirements.txt

REM Set PYTHONPATH to include the top-level project folder
set PYTHONPATH=%PYTHONPATH%;%cd%

REM Run main.py
python src\main.py
