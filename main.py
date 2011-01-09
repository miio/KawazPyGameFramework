# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from libs.core import *
#from libs.utils import *

class MainScene(Scene):
    def __init__(self):
        self.image = Image(0,0,100,100,u"resources/kawaz.png")
    
    def act(self):
        self.image.x += 10
        
    def render(self):
        self.image.render()

def main():
    pygame.init() # pygameの初期化
    Game.get_scene_manager().set_scenes([MainScene()])
    return Game.mainloop()
    #image = Image(0,0,100,100,"resources/kawaz.png")
    #Game.mainloop()

if __name__ == '__main__': main()