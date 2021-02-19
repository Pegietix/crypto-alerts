from django.urls import path

from backend.apps.alerts.views import StartDispatchAlertsJobsView
from backend.apps.alerts.views import StopDispatchAlertsJobsView

urlpatterns = [
    path('dispatch/start/', StartDispatchAlertsJobsView.as_view()),
    path('dispatch/stop/', StopDispatchAlertsJobsView.as_view()),
]
