# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame

from classes.label import Label


class Highscore():

    def __init__(self, screen, results):
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.font_size = self.screen_height / 9
        self.font = pygame.font.Font('fonts/UbuntuMono.ttf', self.font_size)
        self.format = '%d. %s: %s'

        self.results = results
        self.sorted_results = sorted(self.results, key=lambda x: (self.results[x]['time']))

        self.highscore_title = Label('Highscore', self.font, (255, 134, 48))
        highscore_height = (len(results) + 1) * self.highscore_title.height
        self.highscore_title.set_position(
            (self.screen_width / 2) - (self.highscore_title.width / 2),
            (self.screen_height / 2) - (highscore_height / 2)
        )

        self.items = []

        for index, player in enumerate(self.sorted_results):
            highscore_item = Label(self.format % (index + 1, player, results[player]['time']), self.font, (255, 255, 255))
            pos_x = (self.screen_width / 2) - (highscore_item.width / 2)
            pos_y = (self.screen_height / 2) - (highscore_height / 2) + (((index + 1)*2) + (index + 1) * highscore_item.height)
            highscore_item.set_position(pos_x, pos_y)
            self.items.append(highscore_item)

    def render(self, deltat):
        self.screen.blit(self.highscore_title.label, self.highscore_title.position)
        for item in self.items:
            self.screen.blit(item.label, item.position)