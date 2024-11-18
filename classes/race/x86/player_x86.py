# -*- coding: utf-8 -*-
# !/usr/bin/python

from classes.race.player import Player
from classes.race.x86.bike_observer_x86 import BikeObserverX86


class PlayerX86(Player):

    def __init__(self, screen, name, color, pos_x, pos_y, race_length, diameter, parport, parfunc, background=''):
        # Super-Klassen-Aufruf
        Player.__init__(self, screen, name, color, pos_x, pos_y, race_length, diameter, background)

        # Port festlegen und GPIO aktivieren
        self.parport = parport
        self.parfunc = parfunc
        self.bike_observer = BikeObserverX86(self.parport, self.parfunc)

    def update(self, deltat):
        Player.handle_progress(self, self.bike_observer.read_count())
        Player.update(self, deltat)

    def handle_progress(self, ticks):
        if self.event_count >= self.full_ticks:
            self.bike_observer.stop_listening()
        Player.handle_progress(self, ticks)
