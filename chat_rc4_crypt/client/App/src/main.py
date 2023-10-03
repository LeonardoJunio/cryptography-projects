"""Script for Tkinter GUI chat client."""

import os

from src.domain.Client import *

# Adjustment for docker operation, when DISPLAY variable is not found
if os.environ.get('DISPLAY', '') == '':
    # print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

Client().init()
