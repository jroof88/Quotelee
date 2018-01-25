from apscheduler.schedulers.blocking import BlockingScheduler
from util.daily_quote import send_daily_quote

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-sun', hour=19, minute=35)
def scheduled_job():
    print("Sending Out Daily Quote")
    send_daily_quote()

sched.start()