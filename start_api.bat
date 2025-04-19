@echo off
cd /d %~dp0
echo Starting API server in a new window...
start "Uvicorn API Server" cmd /k "call venv\Scripts\activate.bat && start http://127.0.0.1:8000/docs && uvicorn main:app --reload"