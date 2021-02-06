import os


MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
GLASSNODE_API_KEY = os.getenv('GLASSNODE_API_KEY')

FEES_ENDPOINT = 'https://api.glassnode.com/v1/metrics/fees/volume_mean'
BTC_PRICE_ENDPOINT = 'https://api.glassnode.com/v1/metrics/market/price_usd'

MAILGUN_DOMAIN = 'sandbox77e3f720000b476989a9e4ee4f0a041f.mailgun.org'
MAILGUN_ENDPOINT = f'https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages'

FEE_THRESHOLD = 20
BTC_PRICE_THRESHOLD = 45000
RECIPIENTS = ('piotr.goldys9@gmail.com', 'pegietix@gmail.com')
CRONJOB_INTERVAL = 1*60*60*24   # 24h
