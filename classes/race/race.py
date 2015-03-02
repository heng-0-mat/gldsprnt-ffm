# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame
import time
from classes.race.player import Player
from classes.race.label import Label

WHITE = (255, 255, 255)


class Race():

    def __init__(self, screen, players, race_length, diameter):
        self.race_status = 'READY'

        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.font_size = self.screen_height / 9
        self.color_first_player = (255, 85, 0)
        self.color_second_player = (88, 89, 178)
        self.font = pygame.font.Font('fonts/UbuntuMono.ttf', self.font_size)

        self.race_length = race_length
        self.diameter = diameter

        self.players = []
        self.players.append(
            Player(
                self.screen,
                players[0],
                self.color_first_player,
                0,
                0,
                self.race_length,
                self.diameter
            )
        )
        self.players.append(
            Player(
                self.screen,
                players[1],
                self.color_second_player,
                0,
                self.screen_height / 2,
                self.race_length,
                self.diameter
            )
        )

        # Informations-Label
        self.information_label = Label(u'Return zum Starten …', self.font, WHITE)
        self.information_label.set_position(
            (self.screen_width / 2) - (self.information_label.width / 2),
            (self.screen_height - self.information_label.height)
        )

    def update(self, deltat):
        for player in self.players:
            player.update()

    def render(self, deltat):
        # Player rendern
        for player in self.players:
            player.render()
        # Info-Label rendern
        self.screen.blit(self.information_label.label, self.information_label.position)

    def get_element_height(self, element):
        return element.get_rect().height

    def get_element_width(self, element):
        return element.get_rect().width

    def set_race_status(self, status):
        self.race_status = status

    def handle_input(self, event):
        if self.race_status == 'READY':
            if event.key == pygame.K_RETURN:
                self.information_label.set_text('')
                self.set_race_status('RUNNING')
                # Startzeiten an Player übermitteln
                for player in self.players:
                    player.running = True
                    player.set_start_time(time.time())

        if event.key == pygame.K_a:
            self.players[0].handle_progress()
        elif event.key == pygame.K_b:
            self.players[1].handle_progress()