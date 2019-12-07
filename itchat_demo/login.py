import itchat
from apscheduler.schedulers.blocking import BlockingScheduler


def login():
    itchat.auto_login(hotReload=True)


def print_time():
    print('1')


if __name__ == "__main__":
    scheduler = BlockingScheduler()
    scheduler.add_job(print_time, 'date', run_date='2019-12-7 14:35:00')
    scheduler.start()
