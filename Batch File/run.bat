cd /D "%~dp0"
call activate base
python test.py /W

call conda deactivate
pause