from apscheduler.schedulers.background import BackgroundScheduler
from util.daily_quote import send_daily_quote

sched = BackgroundScheduler()

@sched.scheduled_job('cron', hour=12, minute=40, timezone='US/Pacific')
def send_daily_quote_job():
    print("Sending Out Daily Quote from Cron PST")
    send_daily_quote()
    
sched.start()
