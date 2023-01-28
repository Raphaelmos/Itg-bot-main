@echo off

rd /s /q __pycache__
rd /s /q cogs\__pycache__
del settings.db
python main.py
pause