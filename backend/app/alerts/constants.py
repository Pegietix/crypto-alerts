import os


MAILGUN_API_KEY = os.getenv('MAILGUN_API_KEY')
GLASSNODE_API_KEY = os.getenv('GLASSNODE_API_KEY')

FEE_THRESHOLD = 20
BTC_PRICE_THRESHOLD = 45000
RECIPIENTS = ('piotr.goldys9@gmail.com', 'pegietix@gmail.com')
CRONJOB_INTERVAL = 1*60*60*24   # 24h
