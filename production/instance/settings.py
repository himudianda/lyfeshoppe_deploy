ANALYTICS_GOOGLE_UA = 'XXX'

SERVER_NAME = 'lyfeshoppe.com'

SECRET_KEY = 'nevergivethisoutandmakesureitiscomplexdonotusewhatyouseehereseriouslystopreadingandmakearealtoken'
DEBUG = False
LOG_LEVEL = 'INFO'

db_uri = 'postgresql://lyfeshoppe:pass@postgres:5432/lyfeshoppe'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_POOL_SIZE = 25

CACHE_REDIS_URL = 'redis://redis:6379/0'

CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'
CELERY_REDIS_MAX_CONNECTIONS = 25

# Mail settings.
MAIL_USERNAME = 'invincible999@gmail.com'
MAIL_PASSWORD = 'qaWSer12'

# Stripe settings.
STRIPE_SECRET_KEY = 'sk_test_qiyNl7uKGcZur3kBFbZ8CHYm'
STRIPE_PUBLISHABLE_KEY = 'pk_test_dwxVrnUVeaWrsUJEKYH3euhB'

# Twitter settings.
TWITTER_CONSUMER_KEY = 'O3ULXdFEzQO7sn9gqLxKOcl3w'
TWITTER_CONSUMER_SECRET = 'CNXpCbxyyWU3iy9JlO0IqpZuTAZyQnUVFczn35lV1HCAxsGyKr'
TWITTER_ACCESS_TOKEN = '3972337814-uZ17beJg9IM4SBnunN7GGXCZofpmZe9LVQqqX0E'
TWITTER_ACCESS_SECRET = 'Oiw3ghLGQz6PNEJi8VsCwlpSXZHB1uO3WbTpkSO9voEFe'

BROADCAST_PUBLIC_URL = 'https://lyfeshoppe.com/faye/stream'
BROADCAST_INTERNAL_URL = 'http://faye:4242/stream'
BROADCAST_PUSH_TOKEN = 'thistokenneedstomatchtheoneinyourinstancesettingspy'

ENDPOINT_FLOWER = 'https://lyfeshoppe.com/flower'
