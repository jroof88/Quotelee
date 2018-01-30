from apscheduler.schedulers.blocking import BlockingScheduler
from util.daily_quote import send_daily_quote

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=16, minute=39, timezone='US/Pacific')
def send_daily_quote_job():
    send_daily_quote()
    
sched.start()
