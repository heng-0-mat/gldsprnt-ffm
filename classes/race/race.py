# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame

from classes.race.progress import Progress


class Race():

    def __init__(self, screen, players, race_length):
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.font_size = self.screen_height / 9
        self.color_first_player = (255, 85, 0)
        self.color_second_player = (88, 89, 178)
        self.font = pygame.font.Font('fonts/UbuntuMono.ttf', self.font_size)

        self.players = players

        self.race_length = race_length
        self.event_count_first_player = 0
        self.event_count_second_player = 0

        # Namenslabel der Spieler
        self.label_first_player = self.font.render(self.players[0], 1, self.color_first_player)
        self.label_first_player_position = (
            (self.screen_width / 2) - (self.get_element_width(self.label_first_player) / 2),
            self.screen_height / 40
        )
        self.label_second_player = self.font.render(self.players[1], 1, self.color_second_player)
        self.label_second_player_position = (
            (self.screen_width / 2) - (self.get_element_width(self.label_second_player) / 2),
            self.screen_height - self.get_element_height(self.label_second_player) - self.screen_height / 40
        )

        # Progress-Bars für die Spieler
        self.progress_bar_first_player = Progress(
            self.screen,
            self.color_first_player,
            self.screen_width / 80,
            self.screen_height / 2 - self.screen_height / 10 - self.screen_height / 40
        )
        self.progress_bar_second_player = Progress(
            self.screen,
            self.color_second_player,
            self.screen_width / 80,
            self.screen_height / 2 + self.screen_height / 40
        )

        # Progress der Spieler
        self.progress_first_player = 0.0
        self.progress_second_player = 0.0

    def update(self, deltat):
        # Update Progress
        self.progress_bar_first_player.set_progress(self.progress_first_player)
        self.progress_bar_second_player.set_progress(self.progress_second_player)

    def render(self, deltat):
        self.screen.blit(self.label_first_player, self.label_first_player_position)
        self.screen.blit(self.label_second_player, self.label_second_player_position)

        # Progress-Bars
        self.progress_bar_first_player.render()
        self.progress_bar_second_player.render()

    def get_element_height(self, element):
        return element.get_rect().height

    def get_element_width(self, element):
        return element.get_rect().width

    def handle_input(self, event):
        if event.key == pygame.K_a:
            self.event_count_first_player = max(0, min(self.event_count_first_player + 1, self.race_length))
            self.progress_first_player = self.event_count_first_player * 1.0 / self.race_length
        elif event.key == pygame.K_b:
            self.event_count_second_player = max(0, min(self.event_count_second_player + 1, self.race_length))
            self.progress_second_player = self.event_count_second_player * 1.0 / self.race_length