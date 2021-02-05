from backend.app.email_sender import EmailSender
from backend.app.fetcher import GlassnodeDataFetcher
from backend.app.settings import BTC_PRICE_THRESHOLD
from backend.app.settings import FEE_THRESHOLD
from backend.app.settings import RECIPIENTS


def cronjob():
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
