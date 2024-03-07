@echo off
echo Checking for Windows updates...
echo.
echo Please wait...

:: Run Windows Update Check
powershell -command "Get-WindowsUpdate -Online -MicrosoftUpdate -Verbose"

echo.
echo Windows update check complete.
pause
