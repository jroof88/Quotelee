from apscheduler.schedulers.blocking import BlockingScheduler
from util.daily_quote import send_daily_quote

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=3, minute=10, timezone='US/Pacific')
def send_daily_quote_job():
    print("Sending Out Daily Quote from Cron PST")
    send_daily_quote()
    
sched.start()
