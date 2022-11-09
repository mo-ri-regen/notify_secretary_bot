import os
from dotenv import load_dotenv
import discord
from discord.ext import tasks

import notify_bot

load_dotenv()

@tasks.loop(seconds=60)
async def send_message(channel_sent):

    now = notify_bot.get_now()

    if now != os.environ["NOTIFICATION"]:
        return
    
    print("タスク実行中")
    
    weekday = notify_bot.get_weekday()
    text = notify_bot.create_text(weekday)

    embed = discord.Embed(title="コラム担当者おしらせ",description=text, color=0x87CEEB)    
    
    await channel_sent.send(embed=embed)    


client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
# 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    
    channel_sent = client.get_channel(int(os.environ["CHANNEL_ID"]))

    send_message.start(channel_sent) #定期実行するメソッドの後ろに.start()をつける 
    
client.run(os.environ['TOKEN'])
