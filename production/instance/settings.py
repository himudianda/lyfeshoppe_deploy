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
MAIL_USERNAME = 'lyfeshoppe@gmail.com'
MAIL_PASSWORD = 'p7u-wwC-9Hx-JVt'

# Stripe settings.
STRIPE_SECRET_KEY = 'sk_test_qiyNl7uKGcZur3kBFbZ8CHYm'
STRIPE_PUBLISHABLE_KEY = 'pk_test_dwxVrnUVeaWrsUJEKYH3euhB'

ENDPOINT_FLOWER = 'https://lyfeshoppe.com/flower'

# Facebook settings
OAUTH_CREDENTIALS = {
    'facebook': {
        'id': '1737905239773197',
        'secret': '9aa27bf85b54ba749292cee46a013a2f'
    }
}
