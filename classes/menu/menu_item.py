# -*- coding: utf-8 -*-
#!/usr/bin/python

import pygame
from pygame.locals import *

class MenuItem():

    def __init__(self, item, font, font_color, (pos_x, pos_y)=(0, 0)):
        self.item = item
        self.text = self.item[0]
        self.font = font
        self.label = self.font.render(self.text, 1, font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y


    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y

    def set_font_color(self, color):
        self.label = self.font.render(self.text, 1, color)
