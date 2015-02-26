# -*- coding: utf-8 -*-
#!/usr/bin/python

import pygame
from pygame.locals import *

from menu_item import MenuItem

class Menu():

    def __init__(self, screen, items):
        self.font_size = screen.get_height() / (len(items) * 2)
        self.font = pygame.font.Font('fonts/UbuntuMono.ttf', self.font_size)
        self.font_color = (255,255,255)
        self.screen = screen
        self.scr_width = self.screen.get_rect().width
        self.scr_height = self.screen.get_rect().height
        self.items = []
        self.current_item = None
        for index, item in enumerate(items):
            menu_item = MenuItem(item, self.font, self.font_color)

            # t_h: total height of text block
            t_h = len(items) * menu_item.height
            pos_x = (self.scr_width / 2) - (menu_item.width / 2)
            # This line includes a bug fix by Ariel (Thanks!)
            # Please check the comments section of pt. 2 for an explanation
            pos_y = (self.scr_height / 2) - (t_h / 2) + ((index*2) + index * menu_item.height)

            menu_item.set_position(pos_x, pos_y)
            self.items.append(menu_item)


    def update(self):
        self.screen.fill((0,0,0))
        for item in self.items:
            self.screen.blit(item.label, item.position)

    def set_selected_item(self, key):
        for item in self.items:
            item.set_font_color((255,255,255))

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

        self.items[self.current_item].set_font_color((255,0,0))

        if key == pygame.K_SPACE or key == pygame.K_RETURN:
            self.items[self.current_item].item[1]()
