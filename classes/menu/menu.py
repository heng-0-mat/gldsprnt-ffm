# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame
import time
import math

from classes.menu.menu_item import MenuItem
from config import FONT, FONT_MENU

class Menu():
    # Dauer der Animation in Millisekunden
    ANIMATION_DURATION = 250.0

    def __init__(self, screen, items):
        self.font_color = (255, 255, 255)
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.font_size = round(screen.get_height() / 10)
        if self.font_size * len(items) > self.screen_height:
            self.font_size = self.screen_height / (len(items) + 1)
        self.font = pygame.font.Font(FONT_MENU, self.font_size)
        self.items = []
        self.current_item = 0
        self.animating = False
        self.animation_timer = 0
        self.item_margin = 5

        for index, item in enumerate(items):
            menu_item = MenuItem(item, self.font, self.font_color)
            # t_h: total height of text block
            t_h = (len(items) * menu_item.height) + (len(items) * self.item_margin) - self.item_margin
            pos_x = (self.screen_width / 2) - (menu_item.width / 2)
            # This line includes a bug fix by Ariel (Thanks!)
            # Please check the comments section of pt. 2 for an explanation
            pos_y = (self.screen_height / 2) - (t_h / 2) + ((index * self.item_margin) + index * menu_item.height)

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)

    def render(self, deltat):
        # Farben zurücksetzen
        for item in self.items:
            #item.set_font_color((255, 255, 255))
            item.set_default_state()

        #self.items[self.current_item].set_font_color((255, 134, 48))
        self.items[self.current_item].set_active_state()

        # Menuitems rendern
        for item in self.items:
            self.screen.blit(item.label, item.position)

    def handle_keypress(self, key):

        if self.current_item is None:
            self.current_item = 0
        else:
            if key == pygame.K_UP and self.current_item > 0:
                self.current_item -= 1
            elif key == pygame.K_UP and self.current_item == 0:
                self.current_item = len(self.items) - 1
            elif key == pygame.K_DOWN and self.current_item < len(self.items) - 1:
                self.current_item += 1
            elif key == pygame.K_DOWN and self.current_item == len(self.items) - 1:
                self.current_item = 0

        # Werte Hoch und Runter zählen
        if self.items[self.current_item].is_incrementable:
            if key == pygame.K_RIGHT:
                self.items[self.current_item].increment()
            elif key == pygame.K_LEFT:
                self.items[self.current_item].decrement()

            if key == pygame.K_RIGHT or key == pygame.K_LEFT:
                self.items[self.current_item].item["action"]()

        if self.items[self.current_item].has_values:
            if key == pygame.K_RIGHT:
                self.items[self.current_item].select_next_value()
            elif key == pygame.K_LEFT:
                self.items[self.current_item].select_previous_value()

            if key == pygame.K_RIGHT or key == pygame.K_LEFT:
                self.items[self.current_item].item["action"]()

        # Wird ausgeführt, wenn ein Item mit Enter oder Space getriggert wird
        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            self.items[self.current_item].item["action"]()
