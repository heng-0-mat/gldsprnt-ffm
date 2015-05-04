# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame
from pygame import Surface

from classes.label import Label
import classes.helpers as helpers


class Highscore():

    def __init__(self, screen, race_lengths, results, actions, current_item=3):
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.actions = actions

        self.title_font_size = self.screen_height / 12
        self.title_font = pygame.font.Font('fonts/UbuntuMono.ttf', self.title_font_size)
        self.title_format = 'Highscore %dm'
        self.item_format = '%s %s %s %s'

        self.item_offset = 0

        self.results = results
        self.race_lengths = race_lengths
        self.current_race_length = current_item

        self.highscore_title = Label(
            self.title_format % self.race_lengths[self.current_race_length],
            self.title_font,
            (68, 68, 68),
            (255, 255, 255)
        )
        self.highscore_title.set_position(
            (self.screen_width / 2) - (self.highscore_title.width / 2),
            0
        )
        self.highscore_height = self.screen_height - self.highscore_title.height
        self.item_font_size = self.highscore_height / 12
        self.item_font = pygame.font.Font('fonts/UbuntuMono.ttf', self.item_font_size)

        self.item_surface = None
        self.current_highscore_items = None
        self.fill_item_surface()

    def render(self, deltat):
        self.screen.blit(self.item_surface, (
            self.screen_width / 2 - self.item_surface.get_rect().width / 2, self.highscore_title.height
        ))
        self.screen.blit(self.highscore_title.label, self.highscore_title.position)

    def fill_item_surface(self):
        self.current_highscore_items = self.get_highscore_for_length()
        self.item_surface = Surface((self.screen_width, self.highscore_height))
        self.item_surface.fill((68, 68, 68))
        last_item = self.item_offset + 10 if len(self.current_highscore_items) + 10 < len(self.current_highscore_items) else len(self.current_highscore_items)
        position = 0
        for i in range(self.item_offset, last_item):
            player = self.current_highscore_items[i]
            highscore_item = self.item_font.render(
                self.item_format % (
                    str(i + 1).rjust(2),
                    player['name'].ljust(12),
                    helpers.format_time(player['time']).rjust(7),
                    helpers.format_speed(player['speed']).rjust(10)
                ),
                1,
                (255, 255, 255)
            )
            pos_x = (self.screen_width / 2) - (highscore_item.get_rect().width / 2)
            pos_y = position * highscore_item.get_rect().height + highscore_item.get_rect().height / 2
            self.item_surface.blit(highscore_item, (pos_x, pos_y))
            position += 1

    def handle_keypress(self, event):
        if event.key == pygame.K_ESCAPE:
            self.actions['cancel']()
        elif event.key == pygame.K_RIGHT:
            if self.current_race_length + 1 < len(self.race_lengths):
                self.item_offset = 0
                self.current_race_length += 1
                self.fill_item_surface()
                self.highscore_title.set_text(self.title_format % self.race_lengths[self.current_race_length])
                self.highscore_title.set_position(
                    (self.screen_width / 2) - (self.highscore_title.width / 2),
                    0
                )
        elif event.key == pygame.K_LEFT:
            if self.current_race_length > 0:
                self.item_offset = 0
                self.current_race_length -= 1
                self.fill_item_surface()
                self.highscore_title.set_text(self.title_format % self.race_lengths[self.current_race_length])
                self.highscore_title.set_position(
                    (self.screen_width / 2) - (self.highscore_title.width / 2),
                    0
                )
                self.fill_item_surface()

        elif event.key == pygame.K_UP:
            self.item_offset -= 1 if self.item_offset > 0 else 0
            self.fill_item_surface()

        elif event.key == pygame.K_DOWN:
            if self.item_offset + 1 < len(self.current_highscore_items) - 10:
                self.item_offset += 1
            self.fill_item_surface()

    def get_highscore_for_length(self):
        return self.results[self.race_lengths[self.current_race_length]]