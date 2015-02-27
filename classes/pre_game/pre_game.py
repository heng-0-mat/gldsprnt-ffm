# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame


class PreGame():
    def __init__(self, screen, pre_game_item):

        # Screen für Instanz definieren
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        # Label
        self.text = pre_game_item['text']
        # Input-Value
        self.input_value = ''
        self.input_value_text = ''
        self.input_value_cursor = '_'
        self.show_cursor = False
        # Fehler-Text
        self.error_message = ''
        # Font
        self.font_size = self.screen.get_height() / 9
        self.font_color = (255, 255, 255)
        self.font = pygame.font.Font('fonts/UbuntuMono.ttf', self.font_size)
        self.label = self.font.render(self.text, 1, self.font_color)
        self.value_label = self.font.render(self.input_value_text, 1, (255, 134, 48))
        self.error_label = self.font.render(self.error_message, 1, (255, 0, 0))

        # Positionierung der drei Elemente
        total_height = self.get_element_height(self.label) + self.get_element_height(self.value_label) + self.get_element_height(self.error_label)
        self.label_position = self.get_position(self.label, total_height, 0)
        self.value_label_position = self.get_position(self.value_label, total_height, 1)
        self.error_label_position = self.get_position(self.error_label, total_height, 2)

    def update(self, deltat):
        self.value_label = self.font.render(self.input_value_text + self.input_value_cursor, 1, (255, 134, 48))

    def render(self, deltat):
        # Zeilen des PreGame rendern
        self.screen.blit(self.label, self.label_position)
        self.screen.blit(self.value_label, self.value_label_position)
        self.screen.blit(self.error_label, self.error_label_position)

    def handle_keypress(self, key):
        print key

    def get_position(self, element, total_height, order):
        pos_x = (self.screen_width / 2) - (self.get_element_width(element) / 2)
        pos_y = (self.screen_height / 2) - (total_height / 2) + ((order*2) + order * self.get_element_height(element))
        position = (pos_x, pos_y)
        return position

    def get_element_height(self, element):
        return element.get_rect().height

    def get_element_width(self, element):
        return element.get_rect().width