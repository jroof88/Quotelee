from apscheduler.schedulers.blocking import BlockingScheduler
from util.daily_quote import send_daily_quote

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=19, minute=28)
def scheduled_job():
    print("Sending Out Daily Quote")
    send_daily_quote()

sched.start()