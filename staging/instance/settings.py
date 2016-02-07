SERVER_NAME = 'localhost:8081'

DEBUG = False
LOG_LEVEL = 'info'

db_uri = 'postgresql://lyfeshoppe:bestpassword@postgres:5432/lyfeshoppe'
SQLALCHEMY_DATABASE_URI = db_uri

CACHE_REDIS_URL = 'redis://redis:6379/0'

# Celery background worker.
CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'

MAIL_USERNAME = 'you@example.com'
MAIL_PASSWORD = 'thebestpasswordyouevermade'
