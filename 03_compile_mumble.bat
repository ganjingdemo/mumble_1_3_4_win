cd /d %~dp0
set START_TIME=%date% %time%
nmake
set END_TIME=%date% %time%
@echo START_TIME: %START_TIME%
@echo END_TIME:   %END_TIME%
pause