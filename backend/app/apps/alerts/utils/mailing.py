import requests
from django.template.loader import render_to_string

from backend.app.apps.alerts.constants import EMAIL_FROM
from backend.app.apps.alerts.constants import MAILGUN_API_KEY
from backend.app.apps.alerts.constants import MAILGUN_ENDPOINT


class EmailSender:

    def __init__(self, recipients: tuple):
        self.recipients = recipients

    def dispatch_alerts(self, template: str, subject: str, data: dict) -> None:
        for addressee in self.recipients:
            self.send_email_alert(template, subject, addressee, data)

    def send_email_alert(self, template: str, subject: str, addressee: str, data: dict) -> None:
        context = {
            'from': EMAIL_FROM,
            'to': [addressee],
            'subject': subject,
            'html': render_to_string(template, context=data)
        }
        requests.post(MAILGUN_ENDPOINT,  auth=('api', MAILGUN_API_KEY), data=context)
