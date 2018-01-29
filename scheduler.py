from apscheduler.schedulers.blocking import BlockingScheduler
from util.daily_quote import send_daily_quote

sched = BlockingScheduler()
sched.start()

@sched.cron_schedule('cron', hour=11, minute=40)
def scheduled_job():
    print("Sending Out Daily Quote")
    send_daily_quote()