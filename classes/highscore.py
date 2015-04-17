# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame
from pygame import Surface

from classes.label import Label


class Highscore():

    def __init__(self, screen, results, actions):
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.actions = actions

        self.title_font_size = self.screen_height / 12
        self.title_font = pygame.font.Font('fonts/UbuntuMono.ttf', self.title_font_size)
        self.format = '%d. %s: %s'
        self.items_offset = 0

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

        self.item_surface = None
        self.fill_item_surface()

    def render(self, deltat):
        self.screen.blit(self.item_surface, (
            self.screen_width / 2 - self.item_surface.get_rect().width / 2, self.highscore_title.height
        ))
        self.screen.blit(self.highscore_title.label, self.highscore_title.position)

    def fill_item_surface(self):
        self.item_surface = Surface((self.screen_width, self.highscore_height))
        self.item_surface.fill((68, 68, 68))
        first = self.items_offset
        last = self.items_offset + 10 if len(self.results) > self.items_offset + 10 else len(self.results) - 1
        for i in range(first, last):
            player = self.sorted_results[i]
            highscore_item = self.item_font.render(self.format % (i + 1, player['name'], player['speed']), 1, (255, 255, 255))
            pos_x = (self.screen_width / 2) - (highscore_item.get_rect().width / 2)
            pos_y = (i - self.items_offset) * highscore_item.get_rect().height + highscore_item.get_rect().height / 2
            self.item_surface.blit(highscore_item, (pos_x, pos_y))

    def handle_keypress(self, event):
        if event.key == pygame.K_ESCAPE:
            self.actions['cancel']()
        elif event.key == pygame.K_DOWN:
            if len(self.results) > self.items_offset + 10:
                self.items_offset += 10
            self.fill_item_surface()
        elif event.key == pygame.K_UP:
            self.items_offset = self.items_offset - 10 if self.items_offset - 10 > 0 else 0
            self.fill_item_surface()