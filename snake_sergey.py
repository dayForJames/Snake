import pygame as pg
import sys
import random

size = width, height = 800, 600
color = 0, 0, 0

def main():
    pg.init()
    screen = pg.display.set_mode(size)
    gameover = False
    while not gameover:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameover = True
        screen.fill(color)

if __name__ == '__main__':
    main()
