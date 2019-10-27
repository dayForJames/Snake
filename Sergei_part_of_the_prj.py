import pygame as pg
import sys
import random

size = width, height = 800, 600
border_size = 10
color = 180, 212, 101

def rand_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)

def random_position():
    return random.randint(50, 750), random.randint(50, 550)

def create_border(game_surface):
    for i in range(height):
        pg.draw.rect(game_surface, (99, 136, 64), (0, i, 25, 25), 0)
        pg.draw.rect(game_surface, (99, 136, 64), (width - 25, i, 25, 25), 0)
    for i in range(width):
        pg.draw.rect(game_surface, (99, 136, 64), (i, 0, 25, 25), 0)
        pg.draw.rect(game_surface, (99, 136, 64), (i, height - 25, 25, 25), 0)

class Food(object):
    def __init__(self, x_pos_food = None, y_pos_food = None, food_color = None):
        if x_pos_food is None:
            x_pos_food, y_pos_food = random_position()
            food_color = (215, 54, 48)
        self.x_pos_food, self.y_pos_food, self.color = x_pos_food, y_pos_food, food_color

    def is_eaten(self, x, y):
        if x == self.x_pos_food and y == self.y_pos_food:
            self.x_pos_food, self.y_pos_food = random_position()

    def draw_food(self, game_surface):
        pg.draw.rect(game_surface, self.color, (self.x_pos_food, self.y_pos_food, 25, 25), 0)

def main():
    pg.init()
    screen = pg.display.set_mode(size)
    meal = Food()
    gameover = False
    while not gameover:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameover = True
        screen.fill(color)
        create_border(screen)
        meal.draw_food(screen)
        pg.display.flip()
        pg.time.wait(10)
    sys.exit()

if __name__ == '__main__':
    main()
