# -*- coding:utf-8 -*-
import pygame
from pygame.locals import *
from pywaz.window import Window

def main():
    pygame.init() # pygameの初期化
    window = Window(caption=u"Hello,Kawaz!")
    
    while 1:
        for event in pygame.event.get(): # イベントチェック
            if event.type == QUIT: # 終了が押された？
                return
            if (event.type == KEYDOWN and
                event.key  == K_ESCAPE): # ESCが押された？
                return

if __name__ == '__main__': main()