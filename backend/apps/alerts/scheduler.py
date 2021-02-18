from contextlib import suppress

from apscheduler.schedulers import SchedulerAlreadyRunningError
from apscheduler.schedulers import SchedulerNotRunningError
from apscheduler.schedulers.background import BackgroundScheduler
from singleton_decorator import singleton

from backend.apps.alerts.constants import GLASSNODE_ALERTS_INTERVAL
from backend.apps.alerts.constants import REALTIME_ALERTS_INTERVAL
from backend.apps.alerts import AlertDispatcher


@singleton
class Scheduler:
    _scheduler = BackgroundScheduler()
    _alert_dispatcher = AlertDispatcher()

    def __init__(self):
        self._scheduler.add_job(self._alert_dispatcher.dispatch_fee_alerts, 'interval', seconds=GLASSNODE_ALERTS_INTERVAL, id='fee_alerts')
        self._scheduler.add_job(self._alert_dispatcher.dispatch_price_alerts, 'interval', seconds=REALTIME_ALERTS_INTERVAL, id='price_alerts')

    def start_background_jobs(self) -> None:
        try:
            self._scheduler.start()
        except SchedulerAlreadyRunningError:
            self._scheduler.resume()

    def stop_background_jobs(self) -> None:
        with suppress(SchedulerNotRunningError):
            self._scheduler.pause()