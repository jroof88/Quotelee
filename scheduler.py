from apscheduler.schedulers.blocking import BlockingScheduler
from util.daily_quote import send_daily_quote

sched = BlockingScheduler(timezone="US/Pacific")

@sched.scheduled_job('cron', hour=12, minute=13)
def send_daily_quote_job():
    print("Sending Out Daily Quote from Cron 12")
    send_daily_quote()
    
@sched.scheduled_job('cron', hour=4, minute=13)
def send_daily_quote_job():
    print("Sending Out Daily Quote from Cron 4")
    send_daily_quote()
    
sched.start()
