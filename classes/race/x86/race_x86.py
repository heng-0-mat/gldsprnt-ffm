# -*- coding: utf-8 -*-
# !/usr/bin/python


import pygame
import parallel

from classes.race.race import Race
from classes.race.x86.player_x86 import PlayerX86

from config import X86_PARFUNC_PLAYER_1, X86_PARFUNC_PLAYER_2, IMG_PROGRESS_PLAYER_1, IMG_PROGRESS_PLAYER_2, FONT_COLOR_PLAYER_1, FONT_COLOR_PLAYER_2, X86_DEV_PARPORT


class RaceX86(Race):

    def __init__(self, screen, players, race_length, diameter, actions):
        Race.__init__(self, screen, race_length, diameter, actions)

        self.parport = parallel.Parallel(X86_DEV_PARPORT)
        self.parport.setData(0xFF) # supply voltage for sensor -> better get 5V from USB?

        self.players.append(
            PlayerX86(
                self.screen,
                players[0],
                FONT_COLOR_PLAYER_1,
                0,
                0,
                self.race_length,
                self.diameter,
                self.parport,
                X86_PARFUNC_PLAYER_1,
                IMG_PROGRESS_PLAYER_1
            )
        )
        self.players.append(
            PlayerX86(
                self.screen,
                players[1],
                FONT_COLOR_PLAYER_2,
                0,
                self.screen_height / 2,
                self.race_length,
                self.diameter,
                self.parport,
                X86_PARFUNC_PLAYER_2,
                IMG_PROGRESS_PLAYER_2
            )
        )
        print("x86")

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

    def __del__(self):
        try:
            self.parport.__del__()
        except OSError:
            print("Error while releasing Parallel Port")
