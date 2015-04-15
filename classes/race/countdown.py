# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame
import time

from classes.label import Label


class Countdown():

    def __init__(self, screen, actions):

        self.screen = screen
        self.screen_width = screen.get_rect().width
        self.screen_height = screen.get_rect().height
        self.font = pygame.font.Font('fonts/UbuntuMono.ttf', self.screen_height)
        self.start_time = None
        self.running = False
        self.actions = actions
        self.value = 3
        self.label = Label(str(self.value), self.font, (255, 255, 255), (68, 68, 68))
        self.label.set_position(
            self.screen_width / 2 - self.label.width / 2,
            self.screen_height / 2 - self.label.height / 2
        )

    def start(self):
        self.value = 3
        self.label.set_text(str(self.value))
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
                self.label.set_text(str(self.value))
            elif passed_time > 1:
                self.value = 2
                self.label.set_text(str(self.value))

    def render(self, deltat):
        self.screen.blit(self.label.label, self.label.position)