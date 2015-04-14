# -*- coding: utf-8 -*-
# !/usr/bin/python

from classes.race.player import Player
from classes.race.arm.bike_observer import BikeObserver


class PlayerARM(Player):

    def __init__(self, screen, name, color, pos_x, pos_y, race_length, diameter, gpio_port):
        # Super-Klassen-Aufruf
        Player.__init__(self, screen, name, color, pos_x, pos_y, race_length, diameter)

        # Port festlegen und GPIO aktivieren
        self.gpio_port = gpio_port
        self.bike_observer = BikeObserver(self.gpio_port)

    def update(self, deltat):
        current_count = self.bike_observer.read_count()
        self.handle_progress(current_count)
        print current_count
        Player.update(self, deltat)