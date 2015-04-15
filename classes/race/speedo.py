# -*- coding: utf-8 -*-
# !/usr/bin/python

import time

from classes.label import Label


class Speedo():

    def __init__(self, screen, pos_x, pos_y, font, diameter):

        self.screen = screen
        self.screen_width = screen.get_rect().width
        self.screen_height = screen.get_rect().height

        self.format = '%7.2fkm/h'
        self.avg_format = u'ø%6.2fkm/h'
        self.value = 0.0
        self.label_text = self.format % self.value
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.font_size = self.screen_height / 9
        self.font = font

        self.prev_time = int(round(time.time() * 1000))
        self.diameter = diameter

        self.label = Label(self.format % 0.0, self.font, (68, 68, 68), (255, 255, 255), (0, 0), 'speed-grey')
        self.label.set_position(
            self.pos_x + self.screen_width - self.label.width - self.screen_width / 60,
            self.pos_y + self.screen_width / 60
        )

        self.current_ticks = 0

    def update(self):
        self.label.set_text(self.get_current_speed())

    def render(self):
        self.screen.blit(self.label.label, self.label.position)

    def get_current_speed(self):
        current_time = int(round(time.time() * 1000))
        value = (self.format % 0.0)
        if self.prev_time is not None and current_time - self.prev_time < 1000:
            value = self.format % self.value
        return value

    def set_current_speed(self, ticks):
        self.current_ticks += ticks
        if self.current_ticks > 8:
            current_time = int(round(time.time() * 1000))
            self.value = (self.current_ticks * self.diameter * 36.0) / (current_time - self.prev_time)
            self.current_ticks = 0
            self.prev_time = current_time

    def set_avg_speed(self, speed):
        self.label.set_text(self.avg_format % speed)