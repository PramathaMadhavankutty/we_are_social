from base import *
import dj_database_url


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DATABASES['default'] = dj_database_url.parse(
    "mysql://bbf6d3302ef55c:5a72dd57@eu-cdbr-west-01.cleardb.com/heroku_a9f27171bd7bd62?reconnect=true"
)
# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_mttFwgc78Jk5ShtvskP2RHpG')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_k7CEJxI3Net5oB6i8zyT70Ya')

# Paypal environment variables
SITE_URL = 'https://we-are-social-django.herokuapp.com'
PAYPAL_NOTIFY_URL = 'https://we-are-social-django.herokuapp.com/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'pramatha.madhavankutty@yahoo.com'
