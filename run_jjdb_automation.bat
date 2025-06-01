@echo off
echo.
echo ========================================
echo   JJDB Custom Frame Automation
echo ========================================
echo.
echo Activating Python virtual environment...
call "%~dp0venv_jjdb\Scripts\activate.bat"

echo.
echo Running JJDB frame automation script...
echo Make sure Photoshop is open with normal.psd!
echo.
pause

python "%~dp0jjdb_artlayer_fixed.py"

echo.
echo Automation complete!
pause 