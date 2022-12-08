# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame
import os
from pygame import Surface, Color


class Label():

    def __init__(self, text, font, font_color=(255, 255, 255), bg_color=(68, 68, 68), pos_x=0, pos_y=0, icon=""):
        self.text = text
        self.font = font
        self.font_color = font_color
        self.bg_color = bg_color
        self.icon = icon
        self.label = self.create_label()
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = (self.pos_x, self.pos_y)

    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def set_text(self, text):
        self.text = text
        self.label = self.create_label()
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height

    def create_label(self):
        label_text = self.font.render(self.text, 1, self.font_color)
        # Icon anlegen, falls gesetzt
        label_icon_size = 0
        label_icon_width = 0
        if self.icon != '':
            label_icon_size = label_text.get_rect().height
            label_icon_width = 10
        label_box = Surface((label_text.get_rect().width + label_icon_size + label_icon_width + 40, label_text.get_rect().height + 20))
        label_box.set_alpha(64)
        if self.bg_color is not None:
            label_box.fill(self.bg_color)
        if self.icon == '':
            label_box.blit(label_text, (20, 10))
        else:
            label_icon = pygame.transform.smoothscale(pygame.image.load(os.path.join('icons', '%s.png' % self.icon)), (label_icon_size, label_icon_size))
            # add transparent background box
            label_box.set_alpha(128)
            label_box.blit(label_icon, (20, 10))
            label_box.blit(label_text, (label_icon_size + label_icon_width + 20, 10))
        return label_box

    def set_font_color(self, color):
        self.font_color = color
        self.label = self.create_label()

    def set_background_color(self, color):
        self.bg_color = color
        self.label = self.create_label()
