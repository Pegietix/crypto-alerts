from backend.app.apps.alerts.constants import BTC_PRICE_THRESHOLD
from backend.app.apps.alerts.constants import FEE_THRESHOLD
from backend.app.apps.alerts.constants import RECIPIENTS
from backend.app.apps.alerts.utils.fetchers import CoingeckoFetcher
from backend.app.apps.alerts.utils.fetchers import GlassnodeDataFetcher
from backend.app.apps.alerts.utils.mailing import EmailSender


class AlertDispatcher:
    _sender = EmailSender(RECIPIENTS)

    def dispatch_fee_alerts(self) -> None:
        fetched_data = GlassnodeDataFetcher().get_fetched_data()

        if fetched_data['btc_fee'] > FEE_THRESHOLD or fetched_data['eth_fee'] > FEE_THRESHOLD:
            self._sender.dispatch_alerts('fees_alert.html', 'BTC/ETH Transaction Fees Alert', fetched_data)
            print('Fee alerts successfully sent')

    def dispatch_price_alerts(self) -> None:
        current_price = CoingeckoFetcher().get_current_btc_price()['bitcoin']['usd']
        if current_price > BTC_PRICE_THRESHOLD:
            self._sender.dispatch_alerts('price_alert_simple.html', 'BTC Realtime Price Alert', {'btc_price': current_price})
            print('Price alerts successfully sent')