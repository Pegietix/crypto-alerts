import requests
import json

from requests import Response
from jinja2 import Environment, FileSystemLoader

from secrets import API_KEYS

BASE_PAYLOAD = {
    'api_key': API_KEYS['glassnode'],
    'i': '24h',
}


class GlassnodeDataFetcher:
    FEES_ENDPOINT = 'https://api.glassnode.com/v1/metrics/fees/volume_mean'
    BTC_PRICE_ENDPOINT = 'https://api.glassnode.com/v1/metrics/market/price_usd'

    def get_fetched_data(self) -> dict:
        return {
            'btc_fee': self.get_today_fees('BTC'),
            'eth_fee': self.get_today_fees('ETH'),
            'btc_price': self.get_today_price('BTC'),
        }

    def get_today_price(self, currency: str) -> int:
        response = self._query_glassnode(
            endpoint=self.BTC_PRICE_ENDPOINT,
            payload={**BASE_PAYLOAD, 'a': currency}
        )
        return int(self._get_last_value(response))

    def get_today_fees(self, currency: str) -> float:
        response = self._query_glassnode(
            endpoint=self.FEES_ENDPOINT,
            payload={**BASE_PAYLOAD, 'a': currency, 'c': 'USD'}
        )
        return round(float(self._get_last_value(response)), 2)

    @staticmethod
    def _query_glassnode(endpoint: str, payload: dict) -> Response:
        return requests.get(endpoint, params=payload)

    @staticmethod
    def _get_last_value(response: Response) -> str:
        return json.loads(response.text)[-1].get('v')


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
