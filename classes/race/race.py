# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame


class Race():

    def __init__(self, screen, players):
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.font_size = self.screen_height / 9
        self.color_first_player = (255, 85, 0)
        self.color_second_player = (88, 89, 178)
        self.font = pygame.font.Font('fonts/UbuntuMono.ttf', self.font_size)

        self.players = players

        # Namenslabel der Spieler
        self.label_first_player = self.font.render(self.players[0], 1, self.color_first_player)
        self.label_first_player_position = (
            (self.screen_width / 2) - (self.get_element_width(self.label_first_player) / 2),
            30
        )
        self.label_second_player = self.font.render(self.players[1], 1, self.color_second_player)
        self.label_second_player_position = (
            (self.screen_width / 2) - (self.get_element_width(self.label_second_player) / 2),
            (self.screen_height) - self.get_element_width(self.label_second_player)
        )

    def update(self, deltat):
        # Update Race
        print 'update Race'

    def render(self, deltat):
        self.screen.blit(self.label_first_player, self.label_first_player_position)
        self.screen.blit(self.label_second_player, self.label_second_player_position)

    def get_element_height(self, element):
        return element.get_rect().height

    def get_element_width(self, element):
        return element.get_rect().width