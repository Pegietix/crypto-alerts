from apscheduler.schedulers.blocking import BlockingScheduler

from backend.app.alerts.main import run
from backend.app.alerts.settings import CRONJOB_INTERVAL

scheduler = BlockingScheduler()
scheduler.add_job(run, 'interval', seconds=CRONJOB_INTERVAL)

scheduler.start()
