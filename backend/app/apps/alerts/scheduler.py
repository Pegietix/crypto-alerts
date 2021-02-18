from contextlib import suppress

from apscheduler.schedulers import SchedulerAlreadyRunningError
from apscheduler.schedulers import SchedulerNotRunningError
from apscheduler.schedulers.background import BackgroundScheduler
from singleton_decorator import singleton

from backend.app.apps.alerts.constants import ALERTS_INTERVAL
from backend.app.apps.alerts.utils.alerts import dispatch_alerts


@singleton
class Scheduler:
    _scheduler = BackgroundScheduler()

    def __init__(self):
        self._scheduler.add_job(dispatch_alerts, 'interval', seconds=ALERTS_INTERVAL, id='alerts')

    def start_background_jobs(self):
        try:
            self._scheduler.start()
        except SchedulerAlreadyRunningError:
            self._scheduler.resume()

    def stop_background_jobs(self):
        with suppress(SchedulerNotRunningError):
            self._scheduler.pause()
