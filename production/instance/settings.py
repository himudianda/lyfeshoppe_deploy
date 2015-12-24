ANALYTICS_GOOGLE_UA = 'XXX'

SERVER_NAME = 'lyfeshoppe.com'

SECRET_KEY = 'nevergivethisoutandmakesureitiscomplexdonotusewhatyouseehereseriouslystopreadingandmakearealtoken'
DEBUG = False
LOG_LEVEL = 'INFO'

MAIL_USERNAME = 'you@example.com'
MAIL_PASSWORD = 'thebestpasswordyouevermade'

db_uri = 'postgresql://lyfeshoppe:pass@postgres:5432/lyfeshoppe'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_POOL_SIZE = 25

CACHE_REDIS_URL = 'redis://redis:6379/0'

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_REDIS_MAX_CONNECTIONS = 25

STRIPE_SECRET_KEY = 'XXX'
STRIPE_PUBLISHABLE_KEY = 'XXX'

TWITTER_CONSUMER_KEY = 'XXX'
TWITTER_CONSUMER_SECRET = 'XXX'
TWITTER_ACCESS_TOKEN = 'XXX'
TWITTER_ACCESS_SECRET = 'XXX'

BROADCAST_PUBLIC_URL = 'https://lyfeshoppe.com/faye/stream'
BROADCAST_INTERNAL_URL = 'http://faye:4242/stream'
BROADCAST_PUSH_TOKEN = 'thistokenneedstomatchtheoneinyourinstancesettingspy'

ENDPOINT_FLOWER = 'https://lyfeshoppe.com/flower'
