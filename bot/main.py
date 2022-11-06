#00 ライブラリをインポート
import schedule
from time import sleep

#01 定期実行する関数を準備
def task():
    print("タスク実行中")
    
#02 スケジュール登録
schedule.every(10).seconds.do(task)


#03 イベント実行
while True:
    schedule.run_pending()
    sleep(1)