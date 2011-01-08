# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from libs.pywaz import *

def main():
    pygame.init() # pygameの初期化
    image = Image(0,0,100,100,"resources/kawaz.png")
    while 1:
        image.draw()
        pygame.display.flip()
        for event in pygame.event.get(): # イベントチェック
            if event.type == QUIT: # 終了が押された？
                return
            if (event.type == KEYDOWN and
                event.key  == K_ESCAPE): # ESCが押された？
                return

if __name__ == '__main__': main()