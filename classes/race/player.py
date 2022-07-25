# -*- coding: utf-8 -*-
# !/usr/bin/python

import time
from math import modf

import pygame

from classes.label import Label
from classes.race.progress import Progress
from classes.race.speedo import Speedo


class Player():

    def __init__(self, screen, name, color, pos_x, pos_y, race_length, diameter, background=''):
        self.screen = screen
        self.screen_width = screen.get_rect().width
        self.screen_height = screen.get_rect().height

        self.font = pygame.font.Font('fonts/UbuntuMono.ttf', round(self.screen_height / 12))

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
        self.current_time_text = self.format_time(self.get_current_time())
        self.finish_time = None
        self.avg_speed = None

        # Namenslabel
        self.name_label = Label(self.name, self.font, self.color, (255, 255, 255), (0, 0))
        self.name_label.set_position(
            self.pos_x + self.screen_width / 60,
            self.pos_y + self.screen_width / 60
        )

        # Label für Gewinner
        self.winner_label = Label('Winner', self.font, (68, 68, 68), (255, 255, 255))
        self.winner_label.set_position(
            self.pos_x + self.screen_width / 60,
            self.pos_y + 2 * self.screen_width / 60 + self.name_label.height
        )
        self.winner = False
        self.show_winner = False
        self.winner_ticker = 600

        # Time
        self.time_label = Label(self.current_time_text, self.font, (68, 68, 68), (255, 255, 255), (0, 0), 'time-grey')
        self.time_label.set_position(
            self.pos_x + self.screen_width - self.time_label.width - self.screen_width / 60,
            self.pos_y + self.time_label.height + self.screen_width / 60 + self.screen_width / 60
        )

        # Progress
        self.progress_bar = Progress(
            self.screen,
            self.color,
            pos_x,
            pos_y,
            background
        )

        # Speedo
        self.speedo = Speedo(self.screen, self.pos_x, self.pos_y, self.font, self.diameter)

    def update(self, deltat):
        self.progress_bar.set_progress(self.event_count * 1.0 / self.full_ticks)
        if self.running:
            self.time_label.set_text(self.format_time(self.get_current_time()))
        if not self.finished:
            self.speedo.update()
        if self.winner:
            if self.winner_ticker > 500:
                self.show_winner = not self.show_winner
                self.winner_ticker = 0
            else:
                self.winner_ticker += deltat

    def render(self, deltat):
        self.progress_bar.render()
        self.screen.blit(self.name_label.label, self.name_label.position)
        self.screen.blit(self.time_label.label, self.time_label.position)
        self.speedo.render()
        if self.show_winner:
            self.screen.blit(self.winner_label.label, self.winner_label.position)

    def handle_progress(self, ticks):
        if self.running:
            if self.event_count < self.full_ticks:
                self.event_count += ticks
            else:
                self.finish_time = self.get_current_time()
                self.running = False
                self.finished = True
                self.avg_speed = (self.race_length * 3.6) / self.finish_time
                self.speedo.set_avg_speed(self.avg_speed)
                self.time_label.set_text(self.format_time(self.finish_time))
        self.speedo.set_current_speed(ticks)

    def set_start_time(self, start_time):
        self.start_time = start_time

    def get_current_time(self):
        return time.time() - self.start_time

    def format_time(self, timer):
        seconds = int(timer)
        milli_seconds = int(modf(timer)[0] * 100)
        return ('%0d.%02ds' % (seconds, milli_seconds)).rjust(11)

    def set_winner(self):
        self.winner = True
