from backend.app.alerts.email_sender import EmailSender
from backend.app.alerts.fetcher import GlassnodeDataFetcher
from backend.app.alerts.settings import BTC_PRICE_THRESHOLD
from backend.app.alerts.settings import FEE_THRESHOLD
from backend.app.alerts.settings import RECIPIENTS


def run():
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


# Helps with debugging. Run this file to execute script manually.
if __name__ == '__main__':
    run()
