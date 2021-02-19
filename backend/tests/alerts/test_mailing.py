from unittest.mock import call

from pytest import fixture

from backend.apps.alerts.constants import EMAIL_FROM
from backend.apps.alerts.constants import MAILGUN_API_KEY
from backend.apps.alerts.constants import MAILGUN_ENDPOINT
from backend.apps.alerts.constants import RECIPIENTS
from backend.apps.alerts.utils.mailing import EmailSender

EXAMPLE_FETCHED_DATA = {
    'btc_fee': 17.0,
    'eth_fee': 8.43,
    'btc_price': 35000,
}


class TestEmailSender:
    @fixture()
    def sender(self):
        """Init new _sender before each test."""
        return EmailSender(RECIPIENTS)

    def test_dispatch_alerts(self, mocker, sender):
        api_call = mocker.patch('requests.post')

        example_template_name = 'price_alert.html'
        example_subject = 'Example subject'
        sender.dispatch_alerts(example_template_name, example_subject, EXAMPLE_FETCHED_DATA)

        rendered_html = sender._render_email_template(example_template_name, **EXAMPLE_FETCHED_DATA)
        data_template = (
            {
                'from': EMAIL_FROM,
                'to': [addressee],
                'subject': example_subject,
                'html': rendered_html,
            }
            for addressee in RECIPIENTS
        )
        expected_calls = [
            call(MAILGUN_ENDPOINT, auth=('api', MAILGUN_API_KEY), data=data_) for data_ in data_template
        ]
        api_call.assert_has_calls(expected_calls)
