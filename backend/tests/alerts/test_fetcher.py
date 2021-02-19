import os
from unittest.mock import MagicMock

from pytest import fixture
from pytest import mark
from requests.models import Response

from backend.apps.alerts.constants import FEES_ENDPOINT
from backend.apps.alerts.constants import GLASSNODE_API_KEY
from backend.apps.alerts.constants import PRICE_ENDPOINT
from backend.apps.alerts.utils.fetchers import GlassnodeDataFetcher


class TestFetcher:
    @fixture()
    def fetcher(self):
        """Init new fetcher before each test."""
        return GlassnodeDataFetcher()

    @mark.parametrize(
        'currency, response_content_filename, expected_return',
        [
            ('BTC', 'glassnode_btc_fees_response.json', 17.0),
            ('ETH', 'glassnode_eth_fees_response.json', 8.43),
        ],
    )
    def test_get_today_fees(
        self, mocker, fetcher, currency: str, response_content_filename: str, expected_return: float
    ):
        api_response_mock = self._mock_response(response_content_filename)
        query_glassnode = self._mock_query(mocker, api_response_mock)

        assert fetcher.get_today_fees(currency) == expected_return
        query_glassnode.assert_called_once_with(
            endpoint=FEES_ENDPOINT,
            payload={
                'api_key': GLASSNODE_API_KEY,
                'i': '24h',
                'a': currency,
                'c': 'USD',
            },
        )

    @mark.parametrize(
        'currency, response_content_filename, expected_return',
        [
            ('BTC', 'glassnode_btc_prices_response.json', 39784),
            ('ETH', 'glassnode_eth_prices_response.json', 1676),
        ],
    )
    def test_get_today_price(
        self, mocker, fetcher, currency: str, response_content_filename: str, expected_return: int
    ):
        api_response_mock = self._mock_response(response_content_filename)
        query_glassnode = self._mock_query(mocker, api_response_mock)

        assert fetcher.get_today_price(currency) == expected_return
        query_glassnode.assert_called_once_with(
            endpoint=PRICE_ENDPOINT,
            payload={
                'api_key': GLASSNODE_API_KEY,
                'i': '24h',
                'a': currency,
            },
        )

    @staticmethod
    def _mock_response(response_content_filename: str) -> Response:
        api_response_mock = Response()
        api_response_mock._content = open(
            os.path.join('tests', 'alerts', 'miscellaneous', response_content_filename), 'rb'
        ).read()
        return api_response_mock

    @staticmethod
    def _mock_query(mocker, api_response_mock: Response) -> MagicMock:
        return mocker.patch(
            'backend.apps.alerts.utils.fetchers.GlassnodeDataFetcher._query_glassnode',
            return_value=api_response_mock,
        )
