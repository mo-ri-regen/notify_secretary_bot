import os
from dotenv import load_dotenv
import discord

import schedule
from time import sleep

#01 定期実行する関数を準備
def task():
    print("タスク実行中")
    
#02 スケジュール登録
schedule.every(10).seconds.do(task)

# 接続に必要なオブジェクトを生成
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
# 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

    #03 イベント実行
    while True:
        schedule.run_pending()
        sleep(1)
    
load_dotenv()

client.run(os.environ['TOKEN'])