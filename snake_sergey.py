import pygame as pg
import sys
import random

size = width, height = 800, 600
color = 0, 0, 0

def rand_color():
    return 255, random.randint(0, 255), random.randint(0, 255)

def random_position():
    return random.randint(50, 750), random.randint(50, 550)

class Food(object):
    def __init__(self, x_pos_food = None, y_pos_food = None, food_color = None):
        if x_pos_food is None:
            x_pos_food, y_pos_food = random_position()
            food_color = rand_color()
        self.x_pos_food, self.y_pos_food, self.color = x_pos_food, y_pos_food, food_color

    def draw_food(self, game_surface):
        pg.draw.rect(game_surface, self.color, (self.x_pos_food, self.y_pos_food, 10, 10), 0)

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
        meal.draw_food(screen)
        pg.display.flip()
        pg.time.wait(10)
    sys.exit()

if __name__ == '__main__':
    main()
