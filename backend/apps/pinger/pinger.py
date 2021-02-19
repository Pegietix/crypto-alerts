import requests

from backend.django_settings.settings.base import MAIN_DOMAIN


def ping_project() -> None:
    """Ping project to prevent Heroku from turning it into sleep mode."""
    requests.get(MAIN_DOMAIN)
