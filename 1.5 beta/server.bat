@echo off

rd /s /q __pycache__
rd /s /q cogs\__pycache__
python main.py
pause