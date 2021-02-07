import json

import requests
from requests import Response

from backend.app.alerts.constants import FEES_ENDPOINT
from backend.app.alerts.constants import GLASSNODE_API_KEY
from backend.app.alerts.constants import PRICE_ENDPOINT

BASE_PAYLOAD = {
    'api_key': GLASSNODE_API_KEY,
    'i': '24h',
}


class GlassnodeDataFetcher:

    def get_fetched_data(self) -> dict:
        return {
            'btc_fee': self.get_today_fees('BTC'),
            'eth_fee': self.get_today_fees('ETH'),
            'btc_price': self.get_today_price('BTC'),
        }

    def get_today_price(self, currency: str) -> int:
        response = self._query_glassnode(
            endpoint=PRICE_ENDPOINT,
            payload={**BASE_PAYLOAD, 'a': currency}
        )
        return int(self._get_last_value(response))

    def get_today_fees(self, currency: str) -> float:
        response = self._query_glassnode(
            endpoint=FEES_ENDPOINT,
            payload={**BASE_PAYLOAD, 'a': currency, 'c': 'USD'}
        )
        return round(float(self._get_last_value(response)), 2)

    @staticmethod
    def _query_glassnode(endpoint: str, payload: dict) -> Response:
        return requests.get(endpoint, params=payload)

    @staticmethod
    def _get_last_value(response: Response) -> str:
        return json.loads(response.text)[-1].get('v')