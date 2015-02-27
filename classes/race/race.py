# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame


class Race():

    def __init__(self, screen, players):
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        self.font_size = self.screen_height / 9
        self.font = pygame.font.Font('fonts/UbuntuMono.ttf', self.font_size)

        self.players = players

    def update(self, deltat):
        # Update Race
        print 'update Race'

    def render(self, deltat):
        self.screen.blit(self.font.render(self.players[0] + self.players[1], 1, (255, 255, 255)), (100, 100))