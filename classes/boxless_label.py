# -*- coding: utf-8 -*-
# !/usr/bin/python

from classes.label import Label


class BoxlessLabel(Label):

    def __init__(self, text, font, font_color=(255, 255, 255), bg_color=(68, 68, 68), (pos_x, pos_y)=(0, 0)):
        Label.__init__(self, text, font, font_color, bg_color, (pos_x, pos_y))

    def create_label(self):
        return self.font.render(self.text, 1, self.font_color)