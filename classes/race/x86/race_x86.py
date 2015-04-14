# -*- coding: utf-8 -*-
# !/usr/bin/python


import pygame

from classes.race.race import Race
from classes.race.player import Player


class RaceX86(Race):

    def __init__(self, screen, players, race_length, diameter, actions):
        print('Race running in x86-Test-Mode (Keyboard-Input required)')

        Race.__init__(self, screen, race_length, diameter, actions)

        self.players.append(
            Player(
                self.screen,
                players[0],
                (255, 85, 0),
                0,
                0,
                self.race_length,
                self.diameter
            )
        )
        self.players.append(
            Player(
                self.screen,
                players[1],
                (88, 89, 178),
                0,
                self.screen_height / 2,
                self.race_length,
                self.diameter
            )
        )

    def handle_input_data(self, event):
        # Race-Methode ausführen
        Race.handle_input_data(self, event)

        # Countdown-Status
        if self.race_status == 'COUNTDOWN':
            if event.key == pygame.K_a:
                self.interrupt_countdown(self.players[0])
            elif event.key == pygame.K_b:
                self.interrupt_countdown(self.players[1])
        else:
            if event.key == pygame.K_a:
                self.players[0].handle_progress(1)
            elif event.key == pygame.K_b:
                self.players[1].handle_progress(1)