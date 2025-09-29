import os
from dotenv import load_dotenv

# .envファイルを読み込み
load_dotenv()

# Discord Bot Token
DISCORD_BOT_TOKEN = os.getenv('DISCORD_BOT_TOKEN')

# ボットの設定
BOT_PREFIX = '!'
BOT_DESCRIPTION = '占い機能付きDiscordボット'
