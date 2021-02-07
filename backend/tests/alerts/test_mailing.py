from unittest.mock import call

from pytest import fixture

from backend.app.alerts.constants import EMAIL_FROM
from backend.app.alerts.constants import MAILGUN_API_KEY
from backend.app.alerts.constants import MAILGUN_ENDPOINT
from backend.app.alerts.constants import RECIPIENTS
from backend.app.alerts.mailing import EmailSender

EXAMPLE_FETCHED_DATA = {
    'btc_fee': 17.0,
    'eth_fee': 8.43,
    'btc_price': 35000,
}


class TestEmailSender:

    @fixture()
    def sender(self):
        """Init new fetcher before each test."""
        return EmailSender(RECIPIENTS)

    def test_dispatch_alerts(self, mocker, sender):
        api_call = mocker.patch('requests.post')

        example_template_name = 'price_alert.html'
        example_subject = 'Example subject'
        sender.dispatch_alerts(example_template_name, example_subject, EXAMPLE_FETCHED_DATA)

        data_template = (
            {
                'from': EMAIL_FROM,
                'to': [addressee],
                'subject': example_subject,
                'html': sender._render_email_template(example_template_name, **EXAMPLE_FETCHED_DATA)
            } for addressee in RECIPIENTS
        )
        api_call.assert_has_calls(
            [
                call(
                    MAILGUN_ENDPOINT,
                    auth=('api', MAILGUN_API_KEY),
                    data=data_
                ) for data_ in data_template
            ]
        )
