@echo off
echo Trying to stop all Uvicorn processes...
taskkill /F /IM uvicorn.exe >nul 2>&1
taskkill /F /IM python.exe /FI "WINDOWTITLE eq Uvicorn API Server" >nul 2>&1
echo Done. You can close the browser manually if needed.