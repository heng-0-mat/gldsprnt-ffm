# -*- coding: utf-8 -*-
# !/usr/bin/python

import os
from math import modf


def is_raspberry_pi():
    if os.uname()[4][:3] == 'arm':
        return True
    else:
        return False


def format_time(time):
    seconds = int(time)
    milli_seconds = int(modf(time)[0] * 100)
    return '%0d.%02ds' % (seconds, milli_seconds)


def format_speed(speed):
    return '%.2fkm/h' % speed


def build_dict(seq, key):
    return dict((d[key], dict(d, index=i)) for (i, d) in enumerate(seq))