from django.urls import path

from backend.apps.alerts import StartDispatchAlertsJobsView
from backend.apps.alerts import StopDispatchAlertsJobsView

urlpatterns = [
    path('dispatch/start/', StartDispatchAlertsJobsView.as_view()),
    path('dispatch/stop/', StopDispatchAlertsJobsView.as_view()),
]
