# -*- coding: utf-8 -*-
# !/usr/bin/python

import sys

import pygame
from pygame.locals import *

from classes.menu.menu import Menu
from classes.pre_game.pre_game import PreGame
from classes.race.race import Race


class Gldsprnt():
    def __init__(self):
        # PyGame initialisieren
        pygame.init()

        # Display Init
        pygame.display.init()
        display_info = pygame.display.Info()

        # Screen festlegen (Fullscreen aktiviert)
        self.screen = pygame.display.set_mode((display_info.current_w, display_info.current_h), pygame.FULLSCREEN)

        # Maus deaktivieren
        pygame.mouse.set_visible(False)

        # Fenstertitel
        pygame.display.set_caption('GLDSPRNT')
        # erstes Menü laden

        # Hauptmenü festlegen
        main_menu_items = [
            {'text': 'Rennen', 'action': self.load_first_player_input},
            {'text': 'Optionen', 'action': self.load_options_menu},
            {'text': 'Beenden', 'action': sys.exit},
        ]
        # Optionsmenü festlegen
        options_menu_items = [
            {'text': 'Anzahl Spieler', 'increment': {'min': 2, 'max': 12, 'value': 2, 'format':  u'%s: ‹%d›'}, 'action': self.set_player_count},
            {'text': u'Rennlänge', 'increment': {'min': 100, 'max': 1000, 'value': 100, 'step': 10, 'format': u'%s: ‹%dm›'}, 'action': self.set_race_length},
            {'text': u'Zurück', 'action': self.load_main_menu},
        ]

        # Menü erzeugen
        self.main_menu = Menu(self.screen, main_menu_items)
        self.options_menu = Menu(self.screen, options_menu_items)

        # Aktives Menü festlegen
        self.active_menu = self.main_menu

        # Array für aktive Spieler
        self.current_players = []

        # PreGame für Player1 anlegen
        first_pre_game_item = {'text': 'Name erster Fahrer', 'action': self.load_second_player_input}
        # PreGame für Player2 anlegen
        second_pre_game_item = {'text': 'Name zweiter Fahrer', 'action': self.load_race_view}

        # Player1 PreGame erzeugen
        self.first_pre_game = PreGame(self.screen, first_pre_game_item)
        # Player2 PreGame erzeugen
        self.second_pre_game = PreGame(self.screen, second_pre_game_item)
        # Aktives PreGame festlegen
        self.active_pre_game = self.first_pre_game

        # Race-Objekt erzeugen
        self.race = None

        # Goldsprint Einstellungen
        self.player_count = 2
        self.race_length = 100

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

    def load_first_player_input(self):
        self.set_gamestate("PREGAME")
        self.active_pre_game = self.first_pre_game
        if self.prev_gamestate != "PREGAME":
            self.active_pre_game.input_value = ''

    def load_second_player_input(self):
        self.set_gamestate("PREGAME")
        self.active_pre_game = self.second_pre_game
        self.active_pre_game.input_value = ''

    def load_race_view(self):
        players = [self.first_pre_game.input_value, self.second_pre_game.input_value]
        self.race = Race(self.screen, players, self.race_length)
        self.set_gamestate("GAME")

    def set_player_count(self):
        self.player_count = self.active_menu.items[self.active_menu.current_item].increment_value

    def set_race_length(self):
        self.race_length = self.active_menu.items[self.active_menu.current_item].increment_value

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

            self.active_menu.update(deltat)

        elif self.active_gamestate == "PREGAME":
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.set_gamestate("MENU")
                    else:
                        self.active_pre_game.handle_keypress(event)
            self.active_pre_game.update(deltat)

        elif self.active_gamestate == "GAME":
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.set_gamestate("MENU")
                    # TODO: Zum Testen kann man mit Tasten spielen
                    else:
                        self.race.handle_input(event)
            self.race.update(deltat)

        elif self.active_gamestate == "HIGHSCORE":
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
            # Highscore

    def render(self, deltat):
        self.screen.fill((0, 0, 0))

        if self.active_gamestate == "MENU":
            self.active_menu.render(deltat)

        elif self.active_gamestate == "PREGAME":
            self.active_pre_game.render(deltat)
        elif self.active_gamestate == "GAME":
            self.race.render(deltat)
        #elif self.active_gamestate == "HIGHSCORE":
            # Highscore

        pygame.display.flip()
