@echo off

:awake
set name=main

:start
cd %~dp0

:build
pyinstaller --onefile --icon=python.ico %name%.py

:move
copy dist\%name%.exe %cd%

:delete
del %name%.spec
rmdir /q /s build
rmdir /q /s dist

:end
break

