import pygame
from pygame.locals import *
class Snake:
    def __init__(this):
        this.head[50, 50]
        this.body
    def movement(this,Controls):
        if Controls.snake_direction == "RIGHT":
             this.head[0]+=25
        if Controls.snake_direction == "LEFT":
             this.head[0]-=25
        if Controls.snake_direction == "UP":
             this.head[1]+=25
        if Controls.snake_direction == "DOWN":
             this.head[1]-=25
    def Glory(this):
        pygame.draw.rect(pygame.Color("Red"), pygame.Rect(this.head[0], this.head[1],10,10))
class Control:
    def control(this):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_RIGHT and this.snake_direction != "LEFT":
                    this.snake_direction = "RIGHT"
                elif event.key == K_LEFT and this.snake_direction != "RIGHT":
                    this.snake_direction = "LEFT"
                elif event.key == K_DOWN and this.snake_direction != "UP":
                    this.snake_direction = "DOWN"
                elif event.key == K_UP and this.snake_direction != "DOWN":
                    this.snake_direction = "UP"