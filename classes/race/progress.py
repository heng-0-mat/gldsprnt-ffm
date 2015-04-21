# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame
import os


class Progress():

    def __init__(self, screen, bg_color, pos_x, pos_y, image=""):

        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        # Progress-Bar Farbe
        self.bg_color = bg_color

        # Progress
        self.progress = 0.0

        # Progress-Bar Größe
        self.full_width = self.screen_width
        self.height = self.screen_height/2

        # Progress-Bar Position
        self.pos_x = pos_x
        self.pos_y = pos_y

        # Progress-Bar erstellen
        self.bar = (self.pos_x, self.pos_y, self.current_width(), self.height)

        # HIntergrund für ProgressBar
        self.background_image = None
        if image != '':
            if self.height == 384:
                bg = pygame.image.load(os.path.join('images', image + '_384.png'))
            else:
                bg = pygame.image.load(os.path.join('images', image + '_540.png'))
            self.background_image = bg if self.height == 384 else pygame.transform.smoothscale(bg, (bg.get_rect().width * self.height / bg.get_rect().height, self.height))

    def set_progress(self, progress):
        self.progress = progress
        self.bar = (self.pos_x, self.pos_y, self.current_width(), self.height)

    def current_width(self):
        current_width = 0
        if self.progress > 0.0:
            current_width = (self.full_width * self.progress)
        return current_width

    def render(self):
        if self.current_width() > 0:
            if self.background_image is None:
                pygame.draw.rect(self.screen, self.bg_color, self.bar, 0)
            else:
                cropped = pygame.Surface((self.current_width(), self.height))
                cropped.blit(self.background_image, (0, 0))
                self.screen.blit(cropped, (self.pos_x, self.pos_y))