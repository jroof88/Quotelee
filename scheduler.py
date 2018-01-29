from apscheduler.schedulers.blocking import BlockingScheduler
from util.daily_quote import send_daily_quote

sched = BlockingScheduler()

@sched.scheduled_job('cron', hour=11, minute=47)
def send_daily_quote_job():
    print("Sending Out Daily Quote")
    send_daily_quote()
    
@sched.scheduled_job('interval', minute=3)
def send_daily_quote_job2():
    print("Sending Out Daily Quote")
    send_daily_quote()

sched.start()