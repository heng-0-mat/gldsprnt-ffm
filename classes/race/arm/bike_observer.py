# -*- coding: utf-8 -*-
# !/usr/bin/python

from classes import helpers

if helpers.is_raspberry_pi():
    import RPi.GPIO as GPIO


class BikeObserver():

    def __init__(self, port):

        self.port = port
        self.counter = 0
        if helpers.is_raspberry_pi():
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.port, GPIO.IN)

    def count_up(self, channel):
        self.counter += 1

    def start_listening(self):
        if helpers.is_raspberry_pi():
            GPIO.add_event_detect(self.port, GPIO.FALLING, callback=self.count_up)

    def stop_listening(self):
        if helpers.is_raspberry_pi():
            GPIO.remove_event_detect(self.port)

    def read_count(self):
        result = self.counter
        self.counter = 0
        return result