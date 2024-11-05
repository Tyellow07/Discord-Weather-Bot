# Discord Weather Bot重新運行腳本
source ~/my-discord-bot/venv/bin/activate
pkill -f bot.py
python ~/my-discord-bot/bot.py &
deactivate
