from apscheduler.schedulers.blocking import BackgroundScheduler
from util.daily_quote import send_daily_quote

schedule = BackgroundScheduler(timezone="Pacific Standard Time")

@schedule.scheduled_job('cron', day_of_week='mon-fri', hour=21, minute=35)
def scheduled_job():
    send_daily_quote()

sched.start()

#TWILIO_AUTH_TOKEN=93dd11bb635a7cd93db0ad3ad1b1f562
#TWILIO_ACCOUNT_SID=AC758d54dd40c2ea9cfd57bd7c34a7ebf8
#TWILIO_PHONE_NUMBER=19147524388
