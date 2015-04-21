# -*- coding: utf-8 -*-
# !/usr/bin/python

from classes.race.player import Player
from classes.race.arm.bike_observer import BikeObserver


class PlayerARM(Player):

    def __init__(self, screen, name, color, pos_x, pos_y, race_length, diameter, gpio_port, background=''):
        # Super-Klassen-Aufruf
        Player.__init__(self, screen, name, color, pos_x, pos_y, race_length, diameter, background)

        # Port festlegen und GPIO aktivieren
        self.gpio_port = gpio_port
        self.bike_observer = BikeObserver(self.gpio_port)

    def update(self, deltat):
        Player.handle_progress(self, self.bike_observer.read_count())
        Player.update(self, deltat)

    def handle_progress(self, ticks):
        Player.handle_progress(self, ticks)
        if self.finished:
            self.bike_observer.stop_listening()