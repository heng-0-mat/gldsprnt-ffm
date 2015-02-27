# -*- coding: utf-8 -*-
#!/usr/bin/python

import pygame
import sys
from pygame.locals import *

from classes.menu.menu import Menu

class Gldsprnt():
    def __init__(self):
        pygame.init()

        # Display Init
        pygame.display.init()
        display_info = pygame.display.Info()
        # Screen festlegen (Fullscreen aktiviert)
        # Maus deaktivieren
        pygame.mouse.set_visible(False)
        # Aktives Menü festlegen

        # Fenstertitel
        pygame.display.set_caption('GLDSPRNT')
        # erstes Menü laden

        self.screen = pygame.display.set_mode((display_info.current_w, display_info.current_h), pygame.FULLSCREEN)
        # Menüstruktur festlegen
        main_menu_items = [('Rennen', self.start_race), ('Optionen', self.load_options_menu), ('Beenden', self.exit_program)]
        options_menu_items = [('Unterpunkt', self.start_race), ('Unterpunkt 2', self.load_options_menu), (u'Zurück', self.load_main_menu)]
        # Menü erzeugen
        self.main_menu = Menu(self.screen, main_menu_items)
        self.options_menu = Menu(self.screen, options_menu_items)

        self.active_menu = self.main_menu
        self.active_menu.update()


    def exit_program(self):
        sys.exit()

    def load_options_menu(self):
        self.active_menu = self.options_menu
        self.active_menu.update()

    def load_main_menu(self):
        self.active_menu = self.main_menu
        self.active_menu.update()

    def start_race(self):
        print 'Hier soll in die Rennansicht gewechselt werden.'

    def update(self):
        event = pygame.event.wait()
        if event.type == QUIT:
            return
        if event.type == pygame.KEYDOWN:
            self.active_menu.set_selected_item(event.key)
            self.active_menu.update()
        pygame.display.flip()
