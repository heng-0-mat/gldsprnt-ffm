# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame
from classes.race.race import Race
from classes.race.arm.player_arm import PlayerARM


class RaceARM(Race):

    def __init__(self, screen, players, race_length, diameter, actions):
        print('Race running in ARM-Mode (RaspberryPi with GPIO required!)')

        Race.__init__(self, screen, race_length, diameter, actions)

        self.players.append(
            PlayerARM(
                self.screen,
                players[0],
                self.color_first_player,
                0,
                0,
                self.race_length,
                self.diameter,
                23
            )
        )
        self.players.append(
            PlayerARM(
                self.screen,
                players[1],
                self.color_second_player,
                0,
                self.screen_height / 2,
                self.race_length,
                self.diameter,
                24
            )
        )

    def handle_input_data(self, event):
        if self.race_status != 'COUNTDOWN' and self.race_status != 'FINISHED' and self.race_status == 'READY':
            if event.key == pygame.K_ESCAPE:
                for player in self.players:
                    player.bike_observer.stop_listening()
        Race.handle_input_data(self, event)