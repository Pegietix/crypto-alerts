from apscheduler.schedulers.blocking import BlockingScheduler

from main import cronjob
from settings import CRONJOB_INTERVAL

scheduler = BlockingScheduler()
scheduler.add_job(cronjob, 'interval', seconds=CRONJOB_INTERVAL)

scheduler.start()
