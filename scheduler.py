from apscheduler.scheduler import Scheduler
from util.daily_quote import send_daily_quote

sched = Scheduler()
sched.start()

@sched.cron_schedule('cron', hour=11, minute=40)
def scheduled_job():
    print("Sending Out Daily Quote")
    send_daily_quote()