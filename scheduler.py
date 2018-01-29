from apscheduler.schedulers.blocking import BlockingScheduler
from util.daily_quote import send_daily_quote

sched = BlockingScheduler(timezone="America/California")

@sched.scheduled_job('cron', day_of_week='mon', hour=12)
def send_daily_quote_job():
    print("Sending Out Daily Quote from Cron")
    send_daily_quote()
    
@sched.scheduled_job('cron', day_of_week='mon', hour=12, minute=1)
def send_daily_quote_job():
    print("Sending Out Daily Quote from Cron")
    send_daily_quote()

sched.start()