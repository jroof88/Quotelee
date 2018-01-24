from apscheduler.schedulers.blocking import BlockingScheduler
from util.daily_quote import send_daily_quote

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=21, minute=50)
def scheduled_job():
    print("Sending Out Daily Quote")
    send_daily_quote()

@sched.scheduled_job('interval', day_of_week='mon-fri', minutes=5)
def scheduled_job():
    print("Sending Out Daily Quote")
    send_daily_quote()

sched.start()