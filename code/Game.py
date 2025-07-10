#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Menu import Menu
from code.Const import WIN_HEIGHT, WIN_WIDHT


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDHT, WIN_HEIGHT))

    def run(self, ):
        print('Setup start')
        print('Setup end')

        print('Loop start')
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check for all events
            # for event in pygame.event.get():
            #     if event.type == pygame.QUIT:
            #         print('QUITING...')
            #         pygame.quit()  # close window
            #         quit()  # end pygame
