# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

class Window(object):
    def __init__(self, width=640, height=480, caption=u"Hello, World"):
        self.window = pygame.display.set_mode( (width, height) ) # 画面を作る
        pygame.display.set_caption(caption) # タイトル
        pygame.display.flip() # 画面を反映
