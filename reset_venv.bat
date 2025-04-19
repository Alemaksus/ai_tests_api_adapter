@echo off
echo Removing old virtual environment...
rmdir /s /q venv
echo Creating new virtual environment...
python -m venv venv
call venv\Scripts\activate.bat
echo Installing requirements...
pip install --upgrade pip
pip install -r requirements.txt
echo Virtual environment has been reset and dependencies installed.
pause