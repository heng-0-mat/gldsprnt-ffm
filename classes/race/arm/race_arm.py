# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame
from classes.race.race import Race
from classes.race.arm.player_arm import PlayerARM

from config import ARM_PIN_PLAYER_1, ARM_PIN_PLAYER_2, IMG_BG_PLAYER_1, IMG_BG_PLAYER_2

class RaceARM(Race):

    def __init__(self, screen, players, race_length, diameter, actions):
        Race.__init__(self, screen, race_length, diameter, actions)

        self.players.append(
            PlayerARM(
                self.screen,
                players[0],
                (255, 0, 0),
                0,
                0,
                self.race_length,
                self.diameter,
                PIN_PLAYER_1,
                IMG_BG_PLAYER_1
            )
        )
        self.players.append(
            PlayerARM(
                self.screen,
                players[1],
                (0, 0, 255),
                0,
                self.screen_height / 2,
                self.race_length,
                self.diameter,
                PIN_PLAYER_2,
                IMG_BG_PLAYER_2
            )
        )

    def handle_input_data(self, event):
        if self.race_status != 'FINISHED' and self.race_status != 'COUNTDOWN':
            if event.key == pygame.K_ESCAPE:
                for player in self.players:
                    player.bike_observer.stop_listening()
        Race.handle_input_data(self, event)

    def finish_race(self):
        for player in self.players:
            player.bike_observer.stop_listening()
        Race.finish_race(self)
