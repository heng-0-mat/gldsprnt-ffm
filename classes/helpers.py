# -*- coding: utf-8 -*-
# !/usr/bin/python

import os


def is_raspberry_pi():
    if os.uname()[4][:3] == 'arm':
        return True
    else:
        return False