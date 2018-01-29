from apscheduler.schedulers.blocking import BlockingScheduler
from util.daily_quote import send_daily_quote

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon', hour=11, minute=55)
def send_daily_quote_job():
    print("Sending Out Daily Quote from Cron")
    send_daily_quote()
    
@sched.scheduled_job('cron', day_of_week='mon', hour=11, minute=57)
def send_daily_quote_job():
    print("Sending Out Daily Quote from Cron")
    send_daily_quote()
    
@sched.scheduled_job('interval', minutes=3)
def send_daily_quote_job2():
    print("Sending Out Daily Quote from Interval")
    send_daily_quote()

sched.start()