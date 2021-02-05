import os

import pytest
from requests.models import Response

from backend.app.alerts.fetcher import GlassnodeDataFetcher
from backend.app.secrets import API_KEYS


class TestFetcher:

    @pytest.fixture()
    def fetcher(self):
        """Init new fetcher before each test."""
        return GlassnodeDataFetcher()

    def test_get_today_fees_for_btc(self, mocker, fetcher):
        api_response_mock = Response()
        api_response_mock._content = open(
            os.path.join(
                'tests',
                'alerts',
                'miscellaneous',
                'glassnode_btc_fees_response.json'
            ),
            'rb'
        ).read()
        query_glassnode = mocker.patch(
            'backend.app.alerts.fetcher.GlassnodeDataFetcher._query_glassnode',
            return_value=api_response_mock
        )

        assert fetcher.get_today_fees('BTC') == 17.0
        query_glassnode.assert_called_once_with(
            endpoint=fetcher.FEES_ENDPOINT,
            payload={
                'api_key': API_KEYS['glassnode'],
                'i': '24h',
                'a': 'BTC',
                'c': 'USD',
            }
        )

    def test_get_today_fees_for_eth(self, mocker, fetcher):
        api_response_mock = Response()
        api_response_mock._content = open(
            os.path.join(
                'tests',
                'alerts',
                'miscellaneous',
                'glassnode_eth_fees_response.json'
            ),
            'rb'
        ).read()
        query_glassnode = mocker.patch(
            'backend.app.alerts.fetcher.GlassnodeDataFetcher._query_glassnode',
            return_value=api_response_mock
        )

        assert fetcher.get_today_fees('ETH') == 8.43
        query_glassnode.assert_called_once_with(
            endpoint=fetcher.FEES_ENDPOINT,
            payload={
                'api_key': API_KEYS['glassnode'],
                'i': '24h',
                'a': 'ETH',
                'c': 'USD',
            }
        )

    # TODO: Price tests.
