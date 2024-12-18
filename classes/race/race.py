# -*- coding: utf-8 -*-
# !/usr/bin/python

import time
import pygame

from pygame import Color
from classes.race.countdown import Countdown
from classes.label import Label

from config import FONT

class Race():

    def __init__(self, screen, race_length, diameter, actions):
        self.race_status = 'READY'
        self.actions = actions

        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.font_size = round(self.screen_height / 9)
        self.font = pygame.font.Font(FONT, self.font_size)
        self.information_font = pygame.font.Font(FONT, round(self.font_size * 3 / 7))

        self.race_length = race_length
        self.diameter = diameter

        # Leeres Array für Player, wird in Unterklassen belegt
        self.players = []

        # Informations-Label
        self.information_label = Label(u'Return zum Starten …', self.information_font, (68, 68, 68), (255, 255, 255))
        self.information_label.set_position(
            (self.screen_width / 2) - (self.information_label.width / 2),
            (self.screen_height - self.information_label.height)
        )

        # Countdown
        self.countdown = Countdown(self.screen, {'success': self.start})

    def update(self, deltat):
        for player in self.players:
            player.update(deltat)
        if self.race_status == 'COUNTDOWN':
            self.countdown.update(deltat)
            if self.players[0].falseStart:
                self.interrupt_countdown(self.players[0])
            elif self.players[1].falseStart:
                self.interrupt_countdown(self.players[1])
        if self.race_status == 'RUNNING':
            if self.players[0].finished and self.players[1].finished:
                self.finish_race()
            elif self.players[0].finished:
                self.players[0].set_winner()
            elif self.players[1].finished:
                self.players[1].set_winner()
                
    def render(self, deltat):
        # Player rendern
        for player in self.players:
            player.render(deltat)
        # Info-Label rendern
        if self.race_status == 'READY':
            self.screen.blit(self.information_label.label, self.information_label.position)
        elif self.race_status == 'COUNTDOWN':
            self.countdown.render(deltat)
        elif self.race_status == 'FINISHED':
            self.screen.blit(self.information_label.label, self.information_label.position)

    def set_race_status(self, status):
        self.race_status = status

    def handle_input_data(self, event):
        # Anfangs-Status
        if self.race_status == 'READY':
            if event.key == pygame.K_RETURN:
                self.information_label.set_text(' ')
                self.set_race_status('COUNTDOWN')
                self.countdown.start()
                for player in self.players:
                    player.countdown = True
        if self.race_status == 'FINISHED':
            if event.key == pygame.K_RETURN:
                self.actions['success']()

        # Countdown-Status
        elif self.race_status == 'COUNTDOWN':
            if event.key == pygame.K_ESCAPE:
                self.countdown.stop()
                self.race_status = 'READY'
                self.information_label.set_text(u'Return zum Starten …')
                self.information_label.set_position(
                    (self.screen_width / 2) - (self.information_label.width / 2),
                    (self.screen_height - self.information_label.height)
                )

        # sonstige Status
        else:
            if event.key == pygame.K_ESCAPE:
                self.actions['cancel']()

    def start(self):
        self.set_race_status('RUNNING')
        start_time = time.time()
        # Startzeiten an Player übermitteln
        for player in self.players:
            player.countdown = False
            player.running = True
            player.set_start_time(start_time)

    def interrupt_countdown(self, interrupter):
        self.countdown.stop()
        self.race_status = 'READY'
        format = u'Fehlstart von %s (Return für Neustart …)'
        self.information_label.set_text(format % interrupter.name)
        self.information_label.set_position(
            (self.screen_width / 2) - (self.information_label.width / 2),
            (self.screen_height - self.information_label.height)
        )
        for player in self.players:
            player.countdown = False
            player.falseStart = False

    def finish_race(self):
        self.information_label.set_text(u'Weiter mit Return …')
        self.information_label.set_position(
            (self.screen_width / 2) - (self.information_label.width / 2),
            (self.screen_height - self.information_label.height)
        )
        self.set_race_status('FINISHED')
