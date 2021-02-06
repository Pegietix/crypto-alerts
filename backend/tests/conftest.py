import pytest
import requests

from backend.tests.constants import HTTP_REQUEST_METHODS


@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    """Make sure that no real requests are made during tests."""

    def raise_error():
        raise RuntimeError('Network access not allowed during testing!')

    for method in HTTP_REQUEST_METHODS:
        monkeypatch.setattr(requests, method, lambda *args, **kwargs: raise_error())
