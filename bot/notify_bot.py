import os
from dotenv import load_dotenv
import datetime

def create_text(weekday:int):
    
    load_dotenv()
    
    columnist_id = ''
    
    print("担当者がだれか求める")
    
    if weekday == 0:
        columnist_id = os.environ['MONDAY']
    elif weekday == 1:
        columnist_id = os.environ['TUESDAY']
    elif weekday == 2:
        columnist_id = os.environ['WEDNESDAY']
    elif weekday == 3:
        columnist_id = os.environ['THURSDAY']
    elif weekday == 4:
        columnist_id = os.environ['FRIDAY']
    elif weekday == 5:
        columnist_id = os.environ['SATURDAY']
    else:
        columnist_id = os.environ['SUNDAY']
    
    return f"今日のコラム担当者は<@{columnist_id}>です"

# 曜日取得
# 月曜日:0...日曜日:6
def get_weekday():
    
    return datetime.date.today().weekday()
