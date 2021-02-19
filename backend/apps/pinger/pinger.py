import requests


def ping_project():
    requests.get('https://pitu-alerts.herokuapp.com')
