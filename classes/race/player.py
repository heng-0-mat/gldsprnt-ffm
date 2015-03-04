# -*- coding: utf-8 -*-
# !/usr/bin/python

import time
from math import modf

import pygame

from classes.label import Label
from classes.race.progress import Progress
from classes.race.speedo import Speedo


class Player():

    def __init__(self, screen, name, color, pos_x, pos_y, race_length, diameter):
        self.screen = screen
        self.screen_width = screen.get_rect().width
        self.screen_height = screen.get_rect().height

        self.font = pygame.font.Font('fonts/UbuntuMono.ttf', self.screen_height / 9)

        self.race_length = race_length
        self.diameter = diameter

        self.color = color
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.event_count = 0
        self.full_ticks = (self.race_length * 100) / self.diameter
        self.running = False
        self.finished = False
        self.start_time = time.time()
        self.current_time_text = self.get_current_time()
        self.finish_time = None

        # Namenslabel
        self.name_label = Label(self.name, self.font, (255, 255, 255))
        self.name_label.set_position(
            self.pos_x + self.screen_width / 80,
            self.pos_y
        )

        # Time
        self.time_label = Label(self.current_time_text, self.font, (255, 255, 255))
        self.time_label.set_position(
            self.pos_x + self.screen_width - self.time_label.width,
            self.pos_y + self.time_label.height
        )

        # Progress
        self.progress_bar = Progress(
            self.screen,
            self.color,
            pos_x,
            pos_y
        )

        # Speedo
        self.speedo = Speedo(self.screen, self.pos_x, self.pos_y, self.font, self.diameter)

    def update(self):
        self.progress_bar.set_progress(self.event_count * 1.0 / self.full_ticks)
        if self.running:
            self.time_label.set_text(self.get_current_time())
        self.speedo.update()

    def render(self):
        self.progress_bar.render()
        self.screen.blit(self.name_label.label, self.name_label.position)
        self.screen.blit(self.time_label.label, self.time_label.position)
        self.speedo.render()

    def handle_progress(self):
        if self.running:
            if self.event_count < self.race_length:
                self.event_count += 1
            else:
                self.finish_time = self.get_current_time()
                self.running = False
                self.finished = True
                self.time_label.set_text(self.finish_time)
        self.speedo.set_current_speed()

    def set_start_time(self, start_time):
        self.start_time = start_time

    def get_current_time(self):
        timer = time.time() - self.start_time
        seconds = int(timer)
        milli_seconds = int(modf(timer)[0] * 100)
        return ('%0d.%02ds' % (seconds, milli_seconds)).rjust(7)