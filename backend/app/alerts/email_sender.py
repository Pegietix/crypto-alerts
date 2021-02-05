import requests
from jinja2 import Environment
from jinja2 import FileSystemLoader

from backend.app.secrets import API_KEYS


class EmailSender:
    MAILGUN_DOMAIN = 'sandbox77e3f720000b476989a9e4ee4f0a041f.mailgun.org'
    MAILGUN_ENDPOINT = f'https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages'

    def __init__(self, recipients: tuple):
        self.recipients = recipients

    def dispatch_alerts(self, template: str, subject: str, data: dict) -> None:
        for addressee in self.recipients:
            self.send_email_alert(template, subject, addressee, data)

    def send_email_alert(self, template: str, subject: str, addressee: str, data: dict) -> None:
        requests.post(
            self.MAILGUN_ENDPOINT,
            auth=('api', API_KEYS['mailgun']),
            data={
                'from': f'Pitu Alerts <mailgun@{self.MAILGUN_DOMAIN}>',
                'to': [addressee],
                'subject': subject,
                'html': self._render_email_template(template, **data)
            }
        )

    @staticmethod
    def _render_email_template(template: str, **kwargs):
        return Environment(
            loader=FileSystemLoader('templates')
        ).get_template(template).render(**kwargs)
