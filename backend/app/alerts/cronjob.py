from apscheduler.schedulers.blocking import BlockingScheduler

from backend.app.alerts.main import cronjob
from backend.app.alerts.settings import CRONJOB_INTERVAL

scheduler = BlockingScheduler()
scheduler.add_job(cronjob, 'interval', seconds=CRONJOB_INTERVAL)

scheduler.start()
