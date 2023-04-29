@echo off

call %~dp0venv\scripts\activate
cd %~dp0

set MASTER_ID=MasterID
set CHAT_ID=ChatID
set TOKEN=BotToken

python WakeUp.py

echo NekoBot Strawberry crash!

pause