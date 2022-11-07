import os
from dotenv import load_dotenv
import discord
from discord.ext import tasks

load_dotenv()

#01 定期実行する関数を準備
@tasks.loop(seconds=5)
async def send_message():
    print("タスク実行中")
    await channel_sent.send("5秒経ったよ")

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
# 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    global channel_sent
    channel_sent = client.get_channel(int(os.environ["CHANNEL_ID"]))

    send_message.start() #定期実行するメソッドの後ろに.start()をつける 
    
client.run(os.environ['TOKEN'])
