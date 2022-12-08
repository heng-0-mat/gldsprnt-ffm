# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame
from pygame import Surface
import time

from classes.label import Label

from config import FONT_COUNTDOWN


class Countdown():

    def __init__(self, screen, actions):

        self.screen = screen
        self.screen_width = screen.get_rect().width
        self.screen_height = screen.get_rect().height
        self.font = pygame.font.Font(FONT_COUNTDOWN, self.screen_height)
        self.start_time = None
        self.running = False
        self.actions = actions
        self.value = 3
        self.font_color = (68, 68, 68)
        self.background_color = (255, 255, 255)
        #self.label = Label(str(self.value), self.font, (255, 255, 255), (68, 68, 68))
        self.label = self.create_countdown()

    def start(self):
        self.value = 3
        #self.label.set_text(str(self.value))
        self.label = self.create_countdown()
        self.start_time = time.time()
        self.running = True

    def stop(self):
        self.running = False

    def update(self, deltat):
        if self.running:
            passed_time = time.time() - self.start_time
            if passed_time > 3:
                self.running = False
                self.actions['success']()
            elif passed_time > 2:
                self.value = 1
                self.label = self.create_countdown()
            elif passed_time > 1:
                self.value = 2
                self.label = self.create_countdown()

    def render(self, deltat):
        self.screen.blit(self.label, (0, 0))

    def create_countdown(self):
        background = Surface((self.screen_width, self.screen_height))
        background.fill(self.background_color)
        countdown_value = self.font.render(str(self.value), 1, self.font_color)
        background.blit(
            countdown_value,
            (self.screen_width / 2 - countdown_value.get_rect().width / 2,
             self.screen_height / 2 - countdown_value.get_rect().height / 2)
        )
        return background

    def invert_colors(self):
        new_bg_color = self.font_color
        self.font_color = self.background_color
        self.background_color = new_bg_color
        self.label = self.create_countdown()
