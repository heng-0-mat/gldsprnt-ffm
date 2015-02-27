# -*- coding: utf-8 -*-
#!/usr/bin/python

import pygame
import sys
from pygame.locals import *


from classes.gldsprnt import Gldsprnt




def main():
    instance = Gldsprnt()

    # Event loop
    while 1:
        instance.update()



if __name__ == '__main__':
    main()
