# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame
from classes.pre_game.pre_game_item import PreGameItem

class PreGame():
    def __init__(self, screen, actions):
        # Screen für Instanz definieren
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height

        # Actions
        self.actions = actions

        # PreGameItems
        self.pre_game_items = [
            PreGameItem(self.screen, {'description': 'Spieler 1:'}, 0, 0),
            PreGameItem(self.screen, {'description': 'Spieler 2:'}, 0, self.screen_height / 2)
        ]

        # Aktiven Input festlegen (default: 0 => entspricht erstem Item)
        self.active_input = 0
        self.active_color = (255, 134, 48)
        self.active_cursor = '_'


    def update(self, deltat):
        for pre_game_item in self.pre_game_items:
            pre_game_item.input.set_font_color((255, 255, 255))
        self.pre_game_items[self.active_input].input.set_font_color(self.active_color)

    def render(self, deltat):
        for pre_game_item in self.pre_game_items:
            pre_game_item.render(deltat)

    def handle_keypress(self, event):
        if event.unicode.isalpha():
            self.input_value += event.unicode
        elif event.key == pygame.K_BACKSPACE:
            self.delete_last_input_character()
        elif event.key == pygame.K_RETURN:
            self.actions['success']()
        elif event.key == pygame.K_ESCAPE:
            self.actions['cancel']()
        elif event.key == pygame.K_DOWN:
            self.increment_active_item()
        elif event.key == pygame.K_UP:
            self.decrement_active_item()

    def delete_last_input_character(self):
        self.input_value = self.input_value[:-1]

    def set_active_item(self, input_number):
        self.active_input = input_number

    def increment_active_item(self):
        if self.active_input < len(self.pre_game_items) - 1:
            self.active_input += 1
        else:
            self.active_input = 0

    def decrement_active_item(self):
        if self.active_input > 0:
            self.active_input -= 1
        else:
            self.active_input = len(self.pre_game_items) - 1