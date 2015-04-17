# -*- coding: utf-8 -*-
# !/usr/bin/python

import sys

import pygame
from pygame.locals import *

from classes.menu.menu import Menu
from classes.pre_game.pre_game import PreGame
from classes.race.x86.race_x86 import RaceX86
from classes.race.arm.race_arm import RaceARM
from classes.highscore import Highscore
from classes import helpers

PLATFORM = 'x86'
if helpers.is_raspberry_pi():
    PLATFORM = 'ARM'


class Gldsprnt():
    def __init__(self):
        # PyGame initialisieren
        pygame.init()

        # Display Init
        pygame.display.init()
        display_info = pygame.display.Info()

        # Screen festlegen (Fullscreen aktiviert)
        self.screen = pygame.display.set_mode((1024, 768))#(display_info.current_w, display_info.current_h), pygame.FULLSCREEN)

        # Maus deaktivieren
        pygame.mouse.set_visible(False)

        # Fenstertitel
        pygame.display.set_caption('GLDSPRNT')
        # erstes Menü laden

        # Hauptmenü festlegen
        main_menu_items = [
            {'text': 'Rennen', 'action': self.load_pre_game},
            {'text': 'Highscore', 'action': self.load_highscore},
            {'text': 'Optionen', 'action': self.load_options_menu},
            {'text': 'Beenden', 'action': sys.exit},
        ]

        # Goldsprint Einstellungen
        # self.player_count = 2
        self.race_length = 100
        self.diameter = 32.0

        # Optionsmenü festlegen
        options_menu_items = [
            {'text': u'Rennlänge',
             'values': {'value_list': [10, 100, 250, 500, 1000], 'selected': self.race_length, 'format': u'%s: ‹%dm›'},
             'action': self.set_race_length
             },
            {'text': 'Rollenumfang',
             'increment': {'min': 20.0, 'max': 70.0, 'value': self.diameter, 'step': 0.1, 'format': u'%s: ‹%0.1fcm›'},
             'action': self.set_diameter
             },
            {'text': u'Zurück',
             'action': self.load_main_menu
             }
        ]

        # Dictionary für alle Ergebnisse
        self.results = []

        # Menü erzeugen
        self.main_menu = Menu(self.screen, main_menu_items)
        self.options_menu = Menu(self.screen, options_menu_items)

        # Aktives Menü festlegen
        self.active_menu = self.main_menu

        # PreGame-Objekt erzeugen
        self.pre_game = None

        # Race-Objekt erzeugen
        self.race = None

        # Highscore-Objekt erzeugen
        self.highscore = None


        # Aktiven Gamestate festlegen
        self.active_gamestate = "MENU"
        self.prev_gamestate = self.active_gamestate

    # Action-Methoden
    def load_options_menu(self):
        self.active_menu = self.options_menu
        self.options_menu.current_item = 0

    def load_main_menu(self):
        self.set_gamestate("MENU")
        self.active_menu = self.main_menu

    def load_pre_game(self):
        self.set_gamestate("PREGAME")
        self.pre_game = PreGame(self.screen, {'success': self.load_race_view, 'cancel': self.load_main_menu}, self.results)

    def load_race_view(self):
        players = [
            self.pre_game.pre_game_items[0].input_text,
            self.pre_game.pre_game_items[1].input_text
        ]
        if PLATFORM == 'ARM':
            self.race = RaceARM(
                self.screen,
                players,
                self.race_length,
                self.diameter,
                {'cancel': self.load_main_menu, 'success': self.commit_results}
            )
        elif PLATFORM == 'x86':
            self.race = RaceX86(
                self.screen,
                players,
                self.race_length,
                self.diameter,
                {'cancel': self.load_main_menu, 'success': self.commit_results}
            )
        self.set_gamestate("GAME")

    def load_highscore(self):
        self.highscore = Highscore(self.screen, self.results, {'cancel': self.load_main_menu})
        self.set_gamestate('HIGHSCORE')

    def set_race_length(self):
        self.race_length = self.active_menu.items[self.active_menu.current_item].value

    def set_diameter(self):
        self.diameter = self.active_menu.items[self.active_menu.current_item].increment_value

    def commit_results(self):
        for player in self.race.players:
            self.results.append(
                {'name': player.name,
                 'time': player.finish_time,
                 'speed': player.avg_speed}
            )
        self.results = sorted(self.results, key=lambda x: (int(x['speed'])), reverse=True)[:10]
        self.load_highscore()


    def set_gamestate(self, gamestate):
        self.prev_gamestate = self.active_gamestate
        self.active_gamestate = gamestate

    def update(self, deltat):
        if self.active_gamestate == "MENU":
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.active_menu.handle_keypress(event.key)

        elif self.active_gamestate == "PREGAME":
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.pre_game.handle_keypress(event)
            self.pre_game.update(deltat)

        elif self.active_gamestate == "GAME":
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.race.handle_input_data(event)
            self.race.update(deltat)

        elif self.active_gamestate == "HIGHSCORE":
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    self.highscore.handle_keypress(event)

    def render(self, deltat):
        self.screen.fill((68, 68, 68))

        if self.active_gamestate == "MENU":
            self.active_menu.render(deltat)

        elif self.active_gamestate == "PREGAME":
            self.pre_game.render(deltat)
        elif self.active_gamestate == "GAME":
            self.race.render(deltat)
        elif self.active_gamestate == "HIGHSCORE":
            self.highscore.render(deltat)

        pygame.display.flip()
