# -*- coding: utf-8 -*-
#!/usr/bin/python

import pygame
import sys
from pygame.locals import *

from classes.menu.menu import Menu



def exit_program():
    sys.exit()

def load_options_menu():
    print 'Hier soll das Optionen-Menü geladen werden.'

def start_race():
    print 'Hier soll in die Rennansicht gewechselt werden.'

def main():
    pygame.init()
    # Display Init
    pygame.display.init()
    display_info = pygame.display.Info()
    # Screen festlegen (Fullscreen aktiviert)
    screen = pygame.display.set_mode((display_info.current_w, display_info.current_h), pygame.FULLSCREEN)
    # Maus deaktivieren
    pygame.mouse.set_visible(False)
    # Menüstruktur festlegen
    main_menu_items = [('Rennen', start_race), ('Optionen', load_options_menu), ('Beenden', exit_program)]
    # Menü erzeugen
    main_menu = Menu(screen, main_menu_items)
    # Fenstertitel
    pygame.display.set_caption('GLDSPRNT')
    # erstes Menü laden
    main_menu.update()

    # Event loop
    while 1:
        event = pygame.event.wait()
        if event.type == QUIT:
            return
        if event.type == pygame.KEYDOWN:
            main_menu.set_selected_item(event.key)
            main_menu.update()
        pygame.display.flip()



if __name__ == '__main__':
    main()
