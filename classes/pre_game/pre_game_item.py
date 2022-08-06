# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame
import os
from classes.label import Label
from config import FONT


class PreGameItem():

    def __init__(self, screen, item, pos_x, pos_y, icon=""):
        self.screen = screen
        self.display_height = self.screen.get_height() / 2
        self.display_width = self.screen.get_width()
        self.font_size = round(self.screen.get_height() / 10)
        self.title_size = self.display_height

        self.pos_x = pos_x
        self.pos_y = pos_y

        self.item = item
        self.input_text = ''
        self.input_format = '%s'

        # Player-Bild
        self.player_icon = None
        
        if icon != '':
            image = pygame.image.load(os.path.join('icons', '%s.png' % icon))
            self.player_icon = pygame.transform.smoothscale(
                image,
                (int(image.get_rect().width * self.display_height / image.get_rect().height), int(self.display_height))
            )
            self.player_icon_position = (self.display_width / 2 - self.player_icon.get_rect().width / 2, self.pos_y)

        # Input-Zeile
        self.input_font = pygame.font.Font(FONT, self.font_size)
        self.input = Label(self.input_format % self.input_text, self.input_font, (68, 68, 68), (255, 255, 255))

        self.input.set_position(
            self.display_width / 2 + self.pos_x - self.input.width / 2,
            self.pos_y + self.display_height / 2 - self.input.height / 2
        )

    def activate_input(self):
        self.input_format = '%s_'

    def deactivate_input(self):
        self.input_format = '%s'

    def append_key(self, key):
        if len(self.input_text) < 12:
            self.input_text += key

    def delete_last_char(self):
        self.input_text = self.input_text[:-1]

    def update(self, deltat):
        self.input.set_text(self.input_format % self.input_text)
        self.input.set_position(
            self.display_width / 2 + self.pos_x - self.input.width / 2,
            self.pos_y + self.display_height / 2 - self.input.height / 2
        )

    def render(self, deltat):
        self.screen.blit(self.player_icon, self.player_icon_position)
        self.screen.blit(self.input.label, self.input.position)

    def activate(self):
        self.input.set_font_color((68, 68, 68))
        self.input.set_background_color((255, 255, 255))

    def deactivate(self):
        self.input.set_font_color((68, 68, 68))
        self.input.set_background_color((255, 255, 255))
