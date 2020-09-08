from .base import *

DEBUG = False

SECRET_KEY = 'kDhf P*Y(D*^Y*A &TR83qP(T r7P(*Wydpg 98r'
ALLOWED_HOSTS = ['*'] 

try:
    from .local import *
except ImportError:
    pass
