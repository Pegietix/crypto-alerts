import os

import pytest
import requests

from backend.tests.constants import HTTP_REQUEST_METHODS


@pytest.fixture(autouse=True)
def set_working_dir():
    """Make sure tests are run in correct working dir."""
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture(autouse=True)
def disable_network_calls(monkeypatch):
    """Make sure that no real requests are made during tests."""

    def raise_error():
        raise RuntimeError('Network access not allowed during testing!')

    for method in HTTP_REQUEST_METHODS:
        monkeypatch.setattr(requests, method, lambda *args, **kwargs: raise_error())

    assert 1 == 0
