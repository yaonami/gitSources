import itchat
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
import time

import sendMS


def login():
    itchat.auto_login(hotReload=True)


def print_time():
    print(time.time())


if __name__ == "__main__":
    # scheduler = BlockingScheduler()
    # scheduler = BackgroundScheduler()
    # # scheduler.add_job(print_time, 'date', run_date='2019-12-7 14:35:00')
    # scheduler.add_job(login, 'cron', hour='19', minute='36')
    # # scheduler.add_job(print_time, 'interval', seconds=10)
    # scheduler.add_job(sendMS.sendMsg, 'cron', hour='19', minute='37')
    # scheduler.start()
    # # print_time()
    # while True:
    #     pass
    sendMS.getWeather('太原')

