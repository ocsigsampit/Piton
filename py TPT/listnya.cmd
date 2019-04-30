@ECHO OFF &SETLOCAL
set now=%date:~6,4%%date:~3,2%%date:~0,2%
echo %now%

::(FOR /f "delims=" %%a IN ('dir /b /a-d') DO (
::    FOR /f "tokens=1-3*" %%x IN ('dir /a-d /tc "%%~a"^|findstr "^[0-9]"') DO (
::       ECHO "%%a",%%~ta,%%x %%y %%z
::    )
::))>DIR%%now%%.csv
::TYPE DIR%%now%%.csv
pause