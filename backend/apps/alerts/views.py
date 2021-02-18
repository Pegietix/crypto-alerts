from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from backend.apps.alerts import Scheduler


class StartDispatchAlertsJobsView(APIView):
    http_method_names = ['get']

    def get(self, request):
        Scheduler().start_background_jobs()

        return Response(status=status.HTTP_200_OK)


class StopDispatchAlertsJobsView(APIView):
    http_method_names = ['get']

    def get(self, request):
        Scheduler().stop_background_jobs()

        return Response(status=status.HTTP_200_OK)
