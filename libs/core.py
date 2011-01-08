# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *

class Window(object):
    def __init__(self, width=640, height=480, caption=u"Hello, World"):
        self.window = pygame.display.set_mode( (width, height) ) # 画面を作る
        pygame.display.set_caption(caption) # タイトル
        pygame.display.flip() # 画面を反映
        
    def blit(self, image, imagerect):
        self.window.blit(image, imagerect)

class Rect(object):
    def __init__(self, x=0, y=0, w=100, h=100):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.angle = 0
        self.xscale = 1
        self.yscale = 1
        self.alpha = 1
        self.rect = pygame.rect.Rect(x, y, w, h)
    
    @property
    def x(self):
        return self.rect.x
    
    @property
    def y(self):
        return self.rect.
        
    def act(self):
        pass
    
    def draw(self):
        pass
    
    def rotate(self, n):
        self.angle = n

class Image(Rect):
    def __init__(self, x=0 ,y=0 ,w=100, h=100, path=u""):
        super(Rect,Image).__init__(x,y,w,h)
        self.image = pygame.image.load(path).convert()
        self.rect = self.image.get_rect()
        
    def draw(self, x=None, y=None):
        Game.screen.blit(self.image, self.rect)
        
        
class Game(object):
    screen = Window(caption=u"Hello,Kawaz!")