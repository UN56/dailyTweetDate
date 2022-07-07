import schedule
import time
import os 

def job():
    os.system("python ./main.py")

schedule.every().day.at("00:01").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)