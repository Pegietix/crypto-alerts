from apscheduler.schedulers.blocking import BlockingScheduler

from backend.app.alerts.constants import CRONJOB_INTERVAL
from backend.app.alerts.main import run

scheduler = BlockingScheduler()
scheduler.add_job(run, 'interval', seconds=CRONJOB_INTERVAL)

scheduler.start()
