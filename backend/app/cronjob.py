from apscheduler.schedulers.blocking import BlockingScheduler

from backend.app.main import cronjob
from backend.app.settings import CRONJOB_INTERVAL

scheduler = BlockingScheduler()
scheduler.add_job(cronjob, 'interval', seconds=CRONJOB_INTERVAL)

scheduler.start()
