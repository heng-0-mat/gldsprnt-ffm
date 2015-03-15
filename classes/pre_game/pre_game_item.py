# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame
from classes.label import Label


class PreGameItem():

    def __init__(self, screen, item, pos_x, pos_y):
        self.screen = screen
        self.display_height = self.screen.get_height() / 2
        self.display_width = self.screen.get_width()

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.item = item
        self.input_text = 'fff'

        # Beschreibungs-Zeile
        self.description_font = pygame.font.Font('fonts/UbuntuMono.ttf', self.screen.get_height() / 12)
        self.description = Label(self.item['description'], self.description_font, (255, 255, 255))

        # Input-Zeile
        self.input_font = pygame.font.Font('fonts/UbuntuMono.ttf', self.screen.get_height() / 9)
        self.input = Label(self.input_text, self.input_font, (255, 255, 255))

        # Fehler-Zeile
        self.error_text = 'fehler'
        self.error = Label(self.error_text, self.description_font, (255, 0, 0))

        # Höhe aller Elemente
        self.total_height = self.description.height + self.input.height + self.error.height

        # Labels Positionieren
        self.description.set_position(
            self.display_width / 2 + self.pos_x - self.description.width / 2,
            self.pos_y
        )
        self.input.set_position(
            self.display_width / 2 + self.pos_x - self.input.width / 2,
            self.pos_y + self.description.height + 2
        )
        self.error.set_position(
            self.display_width / 2 + self.pos_x - self.error.width / 2,
            self.pos_y + self.description.height + self.input.height + 4
        )

    def get_position(self, element, order):
        pos_x = self.display_width / 2 - element.width / 2
        pos_y = self.display_height + self.pos_y - self.total_height / 2 + ((order*2) + order * element.height)
        position = (pos_x, pos_y)
        return position

    def render(self, deltat):
        self.screen.blit(self.description.label, self.description.position)
        self.screen.blit(self.input.label, self.input.position)
        self.screen.blit(self.error.label, self.error.position)