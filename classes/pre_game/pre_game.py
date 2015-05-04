# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame
from classes.pre_game.pre_game_item import PreGameItem

class PreGame():
    def __init__(self, screen, actions, players):
        # Screen für Instanz definieren
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        # Actions
        self.actions = actions

        # vorhandene Player-Namen
        self.recent_players = players

        # Validierungsfehler
        self.validation_error = False

        # PreGameItems
        self.pre_game_items = [
            PreGameItem(
                self.screen,
                {'description': 'Spieler 1:'},
                0,
                0,
                'bike-red-c'
            ),
            PreGameItem(
                self.screen,
                {'description': 'Spieler 2:'},
                0,
                self.screen_height / 2,
                'bike-blue-c'
            )
        ]

        # Aktiven Input festlegen (default: 0 => entspricht erstem Item)
        self.active_input = 0
        self.pre_game_items[self.active_input].activate_input()
        self.active_color = (255, 134, 48)
        self.active_cursor = '_'

    def update(self, deltat):
        self.validate_names()
        for pre_game_item in self.pre_game_items:
            pre_game_item.deactivate()
            pre_game_item.update(deltat)
        self.pre_game_items[self.active_input].activate()

    def render(self, deltat):
        for pre_game_item in self.pre_game_items:
            pre_game_item.render(deltat)

    def handle_keypress(self, event):
        if event.unicode.isalpha():
            self.pre_game_items[self.active_input].append_key(event.unicode)
        elif event.key == pygame.K_BACKSPACE:
            self.pre_game_items[self.active_input].delete_last_char()
        elif event.key == pygame.K_RETURN:
            if not self.validation_error:
                self.actions['success']()
        elif event.key == pygame.K_ESCAPE:
            self.actions['cancel']()
        elif event.key == pygame.K_DOWN:
            self.increment_active_item()
        elif event.key == pygame.K_UP:
            self.decrement_active_item()

    def set_active_item(self, input_number):
        self.active_input = input_number

    def increment_active_item(self):
        self.pre_game_items[self.active_input].deactivate_input()
        if self.active_input < len(self.pre_game_items) - 1:
            self.active_input += 1
        else:
            self.active_input = 0
        self.pre_game_items[self.active_input].activate_input()

    def decrement_active_item(self):
        self.pre_game_items[self.active_input].deactivate_input()
        if self.active_input > 0:
            self.active_input -= 1
        else:
            self.active_input = len(self.pre_game_items) - 1
        self.pre_game_items[self.active_input].activate_input()

    def validate_names(self):
        error = False
        for pregame_item in self.pre_game_items:
            if pregame_item.input_text == '':
                error = True
        if error:
            self.validation_error = True
        else:
            self.validation_error = False