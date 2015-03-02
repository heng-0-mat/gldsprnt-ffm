# -*- coding: utf-8 -*-
# !/usr/bin/python

import time
from classes.race.label import Label


class Speedo():

    def __init__(self, screen, pos_x, pos_y, font, diameter):

        self.screen = screen
        self.screen_width = screen.get_rect().width
        self.screen_height = screen.get_rect().height

        self.format = '%0.2fkm/h'
        self.value = 0.0
        self.label_text = self.format % self.value
        self.pos_x = 0
        self.font_size = self.screen_height / 9
        self.font = font

        self.prev_time = None
        self.diameter = diameter

        self.label = Label(self.format % 0.0, self.font, (255, 255, 255))
        self.label.set_position(
            pos_x + self.screen_width - self.label.width,
            pos_y
        )

    def update(self):
        self.label.set_text(self.get_current_speed())

    def render(self):
        self.screen.blit(self.label.label, self.label.position)

    def set_value(self, value):
        self.value = value * 1.0
        self.label_text = self.format % self.value

    def get_current_speed(self):
        current_time = time.time()
        value = self.format % 0.0
        if self.prev_time is not None and current_time - self.prev_time < 1:
            value = self.format % self.value
        return value

    def set_current_speed(self):
        current_time = time.time()
        if self.prev_time is not None:
            self.value = (self.diameter * 36.0) / ((current_time - self.prev_time) * 1000.0)
        self.prev_time = current_time