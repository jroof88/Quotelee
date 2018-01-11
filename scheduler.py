from apscheduler.schedulers.blocking import BackgroundScheduler
from util.daily_quote import send_daily_quote

schedule = BackgroundScheduler(timezone="Pacific Standard Time")

@schedule.scheduled_job('cron', day_of_week='mon-fri', hour=9)
def scheduled_job():
    send_daily_quote()

sched.start()