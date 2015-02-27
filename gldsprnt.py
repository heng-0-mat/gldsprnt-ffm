# -*- coding: utf-8 -*-
# !/usr/bin/python

import pygame

from classes.gldsprnt import Gldsprnt

clock = pygame.time.Clock()

def main():
    # Gldsprnt-Instanz erzeugen
    instance = Gldsprnt()

    # Event loop
    while 1:
        deltat = clock.tick(60)

        instance.update(deltat)
        instance.render(deltat)


if __name__ == '__main__':
    main()
