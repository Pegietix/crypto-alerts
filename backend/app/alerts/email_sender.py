import requests
from jinja2 import Environment
from jinja2 import FileSystemLoader

from backend.app.alerts.constants import MAILGUN_API_KEY
from backend.app.alerts.constants import MAILGUN_DOMAIN
from backend.app.alerts.constants import MAILGUN_ENDPOINT


class EmailSender:

    def __init__(self, recipients: tuple):
        self.recipients = recipients

    def dispatch_alerts(self, template: str, subject: str, data: dict) -> None:
        for addressee in self.recipients:
            self.send_email_alert(template, subject, addressee, data)

    def send_email_alert(self, template: str, subject: str, addressee: str, data: dict) -> None:
        requests.post(
            MAILGUN_ENDPOINT,
            auth=('api', MAILGUN_API_KEY),
            data={
                'from': f'Pitu Alerts <mailgun@{MAILGUN_DOMAIN}>',
                'to': [addressee],
                'subject': subject,
                'html': self._render_email_template(template, **data)
            }
        )

    @staticmethod
    def _render_email_template(template: str, **kwargs) -> Environment:
        return Environment(
            loader=FileSystemLoader('templates')
        ).get_template(template).render(**kwargs)
