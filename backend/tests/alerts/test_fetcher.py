import os

import pytest
from pytest import mark
from requests.models import Response

from backend.app.alerts.fetcher import GlassnodeDataFetcher
from backend.app.constants import GLASSNODE_API_KEY


class TestFetcher:

    @pytest.fixture()
    def fetcher(self):
        """Init new fetcher before each test."""
        return GlassnodeDataFetcher()

    @mark.parametrize(
        'currency, response_content_filename, expected_return',
        [
            ('BTC', 'glassnode_btc_fees_response.json', 17.0),
            ('ETH', 'glassnode_eth_fees_response.json', 8.43)
        ]
    )
    def test_get_today_fees(
            self,
            mocker,
            fetcher,
            currency: str,
            response_content_filename: str,
            expected_return: float
    ):
        api_response_mock = Response()
        api_response_mock._content = open(
            os.path.join(
                'tests',
                'alerts',
                'miscellaneous',
                response_content_filename
            ),
            'rb'
        ).read()
        query_glassnode = mocker.patch(
            'backend.app.alerts.fetcher.GlassnodeDataFetcher._query_glassnode',
            return_value=api_response_mock
        )

        assert fetcher.get_today_fees(currency) == expected_return
        query_glassnode.assert_called_once_with(
            endpoint=fetcher.FEES_ENDPOINT,
            payload={
                'api_key': GLASSNODE_API_KEY,
                'i': '24h',
                'a': currency,
                'c': 'USD',
            }
        )

    # TODO: Price tests.
