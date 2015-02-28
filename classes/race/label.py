# -*- coding: utf-8 -*-
# !/usr/bin/python


class Label():

    def __init__(self, text, font, font_color, (pos_x, pos_y)=(0, 0)):
        self.text = text
        self.label = font.render(self.text, 1, font_color)
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