#coding: utf-8

import os

from settings_tests import *

os.environ['DJANGO_LIVE_TEST_SERVER_ADDRESS'] = 'localhost:8001'

TEST_SERVER_URL = 'http://127.0.0.1:8001'

SKIP_SLOW_TESTS = False
