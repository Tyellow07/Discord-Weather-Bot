# Discord Weather Bot重新運行腳本

# 激活虛擬環境
source ~/my-discord-bot/venv/bin/activate

# 停止當前的 bot 進程
pkill -f bot.py

# 重新運行 bot
python ~/my-discord-bot/bot.py &

# 退出虛擬環境
deactivate
