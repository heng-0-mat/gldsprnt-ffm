# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame
import time

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)


class Countdown():

    def __init__(self, screen, actions):

        self.screen = screen
        self.screen_width = screen.get_rect().width
        self.screen_height = screen.get_rect().height
        self.start_time = None
        self.running = False
        self.current_color = RED
        self.actions = actions
        self.light_radius = self.screen_height / 6
        self.light_position = (self.screen_width / 2, self.screen_height / 2 - 2 * self.light_radius)

    def start(self):
        self.start_time = time.time()
        self.running = True

    def update(self, deltat):
        if self.running:
            passed_time = time.time() - self.start_time
            if passed_time > 3:
                self.running = False
                self.actions['success']()
            elif passed_time > 2:
                self.current_color = GREEN
                self.light_position = (self.screen_width / 2, self.screen_height / 2 + 2 * self.light_radius)
            elif passed_time > 1:
                self.current_color = YELLOW
                self.light_position = (self.screen_width / 2, self.screen_height / 2)

    def render(self, deltat):
        pygame.draw.circle(
            self.screen,
            self.current_color,
            self.light_position,
            self.light_radius
        )