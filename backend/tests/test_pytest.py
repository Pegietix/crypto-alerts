"""This module tests key testing suite assumptions for this project."""

import pytest
import requests

from backend.tests.constants import HTTP_REQUEST_METHODS


class TestRequests:
    def test_real_requests_are_blocked_during_testing(self):
        for method in HTTP_REQUEST_METHODS:
            with pytest.raises(RuntimeError):
                self._perform_request(method)

    @staticmethod
    def _perform_request(method: str) -> None:
        """Make example request with specified method."""
        getattr(requests, method)('https://example.com')
