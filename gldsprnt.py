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
    screen = pygame.display.set_mode((600, 480))
    # Menüstruktur festlegen
    main_menu_items = [('Rennen starten', start_race), ('Optionen', load_options_menu), ('Beenden', exit_program)]
    # Menü erzeugen
    main_menu = Menu(screen, main_menu_items)

    pygame.display.set_caption('PyMenu vom Tim')
    main_menu.update()
    pygame.display.flip()

    # Event loop
    while 1:
        event = pygame.event.wait()
        if event.type == QUIT:
            print 'Will quit'
            return
        if event.type == pygame.KEYDOWN:
            main_menu.set_selected_item(event.key)
            main_menu.update()
        pygame.display.flip()



if __name__ == '__main__':
    main()
