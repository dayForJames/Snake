import pygame as pg
import sys
import random

size = width, height = 500, 500
border_size = 10
color = 180, 212, 101
size_rec = 25

def rand_color(count):
    return random.randint(count, 255), random.randint(count, 255), random.randint(count, 255)

def random_position():
    x, y = (random.randint(2, width // size_rec) - 1) * size_rec, (random.randint(2, height // size_rec) - 1) * size_rec
    if x >= width - size_rec:
        x = width - 2 * size_rec
    if y >= height - size_rec:
        y = height - 2 * size_rec
    return x, y

def create_border(game_surface):
    for i in range(height):
        pg.draw.rect(game_surface, (99, 136, 64), (0, i, size_rec, size_rec), 0)
        pg.draw.rect(game_surface, (99, 136, 64), (width - size_rec, i, size_rec, size_rec), 0)
    for i in range(width):
        pg.draw.rect(game_surface, (99, 136, 64), (i, 0, size_rec, size_rec), 0)
        pg.draw.rect(game_surface, (99, 136, 64), (i, height - size_rec, size_rec, size_rec), 0)

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
        pg.draw.rect(game_surface, self.color, (self.x_pos_food, self.y_pos_food, size_rec, size_rec), 0)

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
