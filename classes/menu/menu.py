# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame
import time
import math

from menu_item import MenuItem


class Menu():
    # Dauer der Animation in Millisekunden
    ANIMATION_DURATION = 250.0

    def __init__(self, screen, items):
        self.font_color = (255, 255, 255)
        self.screen = screen
        self.screen_width = self.screen.get_rect().width
        self.screen_height = self.screen.get_rect().height
        self.font_size = screen.get_height() / 10
        if self.font_size * len(items) > self.screen_height:
            self.font_size = self.screen_height / (len(items) + 1)
        self.font = pygame.font.Font('fonts/UbuntuMono.ttf', self.font_size)
        self.items = []
        self.current_item = 0
        self.animating = False
        self.animation_timer = 0

        for index, item in enumerate(items):
            menu_item = MenuItem(item, self.font, self.font_color)

            # t_h: total height of text block
            t_h = len(items) * menu_item.height
            pos_x = (self.screen_width / 2) - (menu_item.width / 2)
            # This line includes a bug fix by Ariel (Thanks!)
            # Please check the comments section of pt. 2 for an explanation
            pos_y = (self.screen_height / 2) - (t_h / 2) + ((index*2) + index * menu_item.height)

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)

    def update(self, deltat):
        # Überprüft ob die Animation abgelaufen ist
        if self.animating and time.time() * 1000.0 - self.animation_timer > self.ANIMATION_DURATION:
            current_item = self.items[self.current_item]
            current_item.set_position(current_item.prev_position[0], current_item.prev_position[1])

            self.animating = False
            self.animation_timer = 0
            self.items[self.current_item].item["action"]()

    def render(self, deltat):
        # Farben zurücksetzen
        for item in self.items:
            item.set_font_color((255, 255, 255))

        self.items[self.current_item].set_font_color((255, 134, 48))

        # Menuitems rendern
        for item in self.items:
            self.screen.blit(item.label, item.position)

        # Animationen rendern
        if self.animating:
            current_item = self.items[self.current_item]

            px = current_item.prev_position[0]
            py = current_item.prev_position[1]

            # Animations Variablen
            speed = 0.05  # Geschwindigkeit der Animation
            swing_amount = 1.0  # Wie doll der Text wackelt :)

            # t = 0 bei Animationsstart
            t = time.time() * 1000.0 - self.animation_timer

            # DeltaT in der Animation macht die Animation Framerate unabhängig
            px += math.sin(t * speed) * (swing_amount * deltat)

            current_item.position = (px, py)

    def handle_keypress(self, key):
        # Menüitems nicht änderbar während der Animation
        if self.animating:
            return

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
        if self.items[self.current_item].incrementable:
            if key == pygame.K_RIGHT:
                self.items[self.current_item].increment()
            elif key == pygame.K_LEFT:
                self.items[self.current_item].decrement()

            if key == pygame.K_RIGHT or key == pygame.K_LEFT:
                self.items[self.current_item].item["action"]()

        # Wird ausgeführt, wenn ein Item mit Enter oder Space getriggert wird
        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            self.animating = True
            self.animation_timer = time.time() * 1000.0
            # Vorherige Position speichern, um diese nach der Animation zurückzusetzen
            self.items[self.current_item].prev_position = self.items[self.current_item].position
