from backend.app.apps.alerts.constants import BTC_PRICE_THRESHOLD
from backend.app.apps.alerts.constants import FEE_THRESHOLD
from backend.app.apps.alerts.constants import RECIPIENTS
from backend.app.apps.alerts.utils.fetchers import GlassnodeDataFetcher
from backend.app.apps.alerts.utils.mailing import EmailSender


def dispatch_alerts():
    fetched_data = GlassnodeDataFetcher().get_fetched_data()
    sender = EmailSender(RECIPIENTS)

    # Price alerts
    if fetched_data['btc_price'] > BTC_PRICE_THRESHOLD:
        sender.dispatch_alerts('price_alert.html', 'BTC Price Alert', fetched_data)
        print('PRICE alerts successfully sent.')

    # Fee alerts
    elif fetched_data['btc_fee'] > FEE_THRESHOLD or fetched_data['eth_fee'] > FEE_THRESHOLD:
        sender.dispatch_alerts('fees_alert.html', 'BTC/ETH Transaction Fees Alert', fetched_data)
        print('FEE alerts successfully sent.')

    else:
        print('Script successfully terminated without dispatching alerts')
