from apscheduler.schedulers.blocking import BlockingScheduler
from util.daily_quote import send_daily_quote
from pytz import utc

sched = BlockingScheduler(timezone=utc)

@sched.scheduled_job('cron', hour=12, minute=14)
def send_daily_quote_job():
    print("Sending Out Daily Quote from Cron PST")
    send_daily_quote()
    
@sched.scheduled_job('cron', hour=8, minute=14)
def send_daily_quote_job():
    print("Sending Out Daily Quote from Cron UTC")
    send_daily_quote()
    
sched.start()
