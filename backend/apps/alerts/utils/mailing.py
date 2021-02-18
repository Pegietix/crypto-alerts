import requests
from django.template.loader import render_to_string

from backend.apps.alerts.constants import EMAIL_FROM
from backend.apps.alerts.constants import MAILGUN_API_KEY
from backend.apps.alerts.constants import MAILGUN_ENDPOINT


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
            'html': self._render_email_template(template, **data)
        }
        requests.post(MAILGUN_ENDPOINT,  auth=('api', MAILGUN_API_KEY), data=context)

    @staticmethod
    def _render_email_template(template, **kwargs):
        return render_to_string(template, context=kwargs)
