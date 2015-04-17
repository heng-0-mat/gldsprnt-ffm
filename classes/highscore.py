# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame
from pygame import Surface

from classes.label import Label


class Highscore():

    def __init__(self, screen, results):
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.title_font_size = self.screen_height / 12
        self.title_font = pygame.font.Font('fonts/UbuntuMono.ttf', self.title_font_size)
        self.format = '%d. %s: %s'

        self.results = [
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '500'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
            {'name': 'tim', 'time': '1:00', 'speed': '1'},
            {'name': 'tim', 'time': '1:00', 'speed': '1000'},
        ]
        self.sorted_results = sorted(self.results, key=lambda x: (int(x['speed'])))

        self.highscore_title = Label('Highscore', self.title_font, (68, 68, 68), (255, 255, 255))
        self.highscore_title.set_position(
            (self.screen_width / 2) - (self.highscore_title.width / 2),
            (self.screen_height / 11) - (self.highscore_title.height / 2)
        )
        self.highscore_height = self.screen_height - self.screen_height / 11
        self.item_font_size = self.highscore_height / 11
        self.item_font = pygame.font.Font('fonts/UbuntuMono.ttf', self.item_font_size)

        self.item_surface = Surface((self.highscore_height, self.screen_width))
        self.item_surface.fill((68, 68, 68))

        for index, player in enumerate(self.sorted_results):
            #highscore_item = Label(player, self.title_font, (255, 255, 255), (68, 68, 68))
            highscore_item = self.item_font.render(self.format % (index + 1, player['name'], player['speed']), 1, (255, 255, 255))
            pos_x = (self.screen_width / 2) - (highscore_item.get_rect().width / 2)
            pos_y = index * highscore_item.get_rect().height + highscore_item.get_rect().height / 2
            self.item_surface.blit(highscore_item, (pos_x, pos_y))

    def render(self, deltat):
        self.screen.blit(self.item_surface, (
            0, self.highscore_title.height
        ))
        self.screen.blit(self.highscore_title.label, self.highscore_title.position)