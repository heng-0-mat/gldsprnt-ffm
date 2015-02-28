# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame


class Progress():

    def __init__(self, screen, bg_color, pos_x, pos_y):

        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        # Progress-Bar Farbe
        self.bg_color = bg_color

        # Progress
        self.progress = 0.0

        # Progress-Bar Größe
        self.full_width = self.screen_width - self.screen_width / 10
        self.height = self.screen_height / 10

        # Progress-Bar Position
        self.pos_x = pos_x
        self.pos_y = pos_y

        # Progress-Bar erstellen
        self.bar = (self.pos_x + 2, self.pos_y + 2, self.current_width(), self.height - 4)

        # Prgress-Bar Container
        self.container = (self.pos_x, self.pos_y, self.full_width, self.height)

    def set_progress(self, progress):
        self.progress = progress
        self.bar = (self.pos_x + 2, self.pos_y + 2, self.current_width(), self.height - 4)

    def current_width(self):
        current_width = 0
        if self.progress > 0.0:
            current_width = (self.full_width * self.progress) - 4
        return current_width

    def render(self):
        pygame.draw.rect(self.screen, (255, 255, 255), self.container, 0)
        if self.current_width() > 0:
            pygame.draw.rect(self.screen, self.bg_color, self.bar, 0)