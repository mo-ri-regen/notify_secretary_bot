import os
from dotenv import load_dotenv
import datetime

def create_text(tomorrow_weekday:int):
    
    load_dotenv()
    
    columnist_id = ''
    
    print("担当者がだれか求める")
    
    if tomorrow_weekday == 0:
        columnist_id = os.environ['MONDAY']
    elif tomorrow_weekday == 1:
        columnist_id = os.environ['TUESDAY']
    elif tomorrow_weekday == 2:
        columnist_id = os.environ['WEDNESDAY']
    elif tomorrow_weekday == 3:
        columnist_id = os.environ['THURSDAY']
    elif tomorrow_weekday == 4:
        columnist_id = os.environ['FRIDAY']
    elif tomorrow_weekday == 5:
        columnist_id = os.environ['SATURDAY']
    else:
        columnist_id = os.environ['SUNDAY']
    
    return f"明日のコラム担当者は<@{columnist_id}>です\nそれでは今日もCoolな1日を🆒(コピペ用)"

# 曜日取得
# 月曜日:0...日曜日:6
def get_weekday():
    
    print("曜日取得")
    return datetime.date.today().weekday()

def get_tomorrow_weekday(weekday):
    
    return (weekday + 1) % 7

def get_now():
    
    #JST
    return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).strftime('%H:%M')
