import json

import requests
from requests import Response

from backend.app.secrets import API_KEYS

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