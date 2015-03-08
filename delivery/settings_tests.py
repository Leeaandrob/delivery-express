#coding:utf-8
import logging

from settings import *

DEBUG = True

DATABASES = {
        'default': {
                    'ENGINE': 'django.db.backends.sqlite3',
                    'NAME':':memory:',
                }
}


INSTALLED_APPS = list(INSTALLED_APPS)

RUN_SLOW_TESTS = False
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
SKIP_SLOW_TESTS = True
BROKER_BACKEND = 'memory'
