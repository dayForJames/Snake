import pygame as pg
import random
import sys

#   Main constants of the game

size = width, height = 500, 500
border_size = 10
color = 180, 212, 101
border_color = 99, 136, 64
size_rec = 20

#   Game functions of its rules

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
        pg.draw.rect(game_surface, border_color, (0, i, size_rec, size_rec), 0)
        pg.draw.rect(game_surface, border_color, (width - size_rec, i, size_rec, size_rec), 0)
    for i in range(width):
        pg.draw.rect(game_surface, border_color, (i, 0, size_rec, size_rec), 0)
        pg.draw.rect(game_surface, border_color, (i, height - size_rec, size_rec, size_rec), 0)

#   Snake's food as an object

class Food(object):
    def __init__(self, x_pos_food = None, y_pos_food = None, food_color = None):
        if x_pos_food is None:
            x_pos_food, y_pos_food = random_position()
            food_color = (215, 54, 48)
            self.x_pos_food, self.y_pos_food, self.color = x_pos_food, y_pos_food, food_color

    def draw_food(self, game_surface):
        pg.draw.rect(game_surface, self.color, (self.x_pos_food, self.y_pos_food, size_rec, size_rec), 0)

#   Snake

# Set the width and height of each snake segment
segment_width = size_rec
segment_height = size_rec

class Segment(pg.sprite.Sprite):
    """ Class to represent one segment of the snake. """
    # -- Methods
    # Constructor function
    def __init__(self, x, y):
        # Call the parent's constructor
        super().__init__()

        # Set height, width
        self.image = pg.Surface([segment_width, segment_height])
        self.image.fill((31, 89, 207))

        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

#   Functions of menu buttons
#   Main game (Snake)

def startGame(screen):
    pg.display.set_caption('Snake')
    # Margin between each segment
    segment_margin = 0

    # Set initial speed
    x_change = segment_width + segment_margin
    y_change = 0
    allspriteslist = pg.sprite.Group()
    # Create an initial snake
    snake_segments = []
    for i in range(4):
        x = 260 - (segment_width + segment_margin) * i
        y = size_rec
        segment = Segment(x, y)
        snake_segments.append(segment)
        allspriteslist.add(segment)

    clock = pg.time.Clock()
    meal = Food()
    gameover = False
    is_failed = False
    right, left, top, bottom = False, False, False, False
    while not gameover:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameover = True
        # Set the speed based on the key pressed
        # We want the speed to be enough that we move a full
        # segment, plus the margin.
            if event.type == pg.KEYDOWN and not is_failed:
                if event.key == pg.K_a and not right:
                    left = True
                    top, bottom = False, False
                    x_change = (segment_width + segment_margin) * -1
                    y_change = 0
                if event.key == pg.K_d and not left:
                    right = True
                    top, bottom = False, False
                    x_change = (segment_width + segment_margin)
                    y_change = 0
                if event.key == pg.K_w and not bottom:
                    top = True
                    right, left = False, False
                    x_change = 0
                    y_change = (segment_height + segment_margin) * -1
                if event.key == pg.K_s and not top:
                    bottom = True
                    right, left = False, False
                    x_change = 0
                    y_change = (segment_height + segment_margin)
        if not is_failed:
            old_segment = snake_segments.pop()
            allspriteslist.remove(old_segment)

            # Figure out where new segment will be

            x = snake_segments[0].rect.x + x_change
            y = snake_segments[0].rect.y + y_change
            segment = Segment(x, y)

            # Insert new segment into the list

            snake_segments.insert(0, segment)
            allspriteslist.add(segment)

            # -- Draw everything
            # Clear screen

            screen.fill(color)
            create_border(screen)

        #   Checking

        if snake_segments[0].rect.x == meal.x_pos_food and snake_segments[0].rect.y == meal.y_pos_food:
            meal = Food()
            snake_segments.insert(0, segment)
            allspriteslist.add(segment)
        if snake_segments[0].rect.x > width - size_rec * 2 or snake_segments[0].rect.x < size_rec or snake_segments[0].rect.y > height - size_rec * 2 or snake_segments[0].rect.y < size_rec:
            is_failed = True
        for i in range(2, len(snake_segments)):
            if snake_segments[i].rect.x == snake_segments[0].rect.x and snake_segments[i].rect.y == snake_segments[0].rect.y:
                is_failed = True
        meal.draw_food(screen)
        allspriteslist.draw(screen)
        pg.display.flip()

        # Pause

        clock.tick(5)
        if is_failed is True:
            data = 'You lost your snake'
            font = pg.font.Font('8201.ttf', 23)
            screen.blit(font.render(data, False, color), (50, 0))
    sys.exit()

#   For button 'About Us'

def about_us(screen):
    pg.display.set_caption('About Us')
    screen.fill(color)
    create_border(screen)

    #   Menu button
    pg.draw.rect(screen, (0, 100, 140), (width - size_rec, 0, size_rec, size_rec))

    data = 'Developed by:', 'Sergei', 'Petr', 'Mark', 'Menu'
    font = pg.font.Font('8201.ttf', 23)
    count = 0
    screen.blit(font.render(data[4], False, color), (width - size_rec * 4, 0))
    for i in range(4):
        screen.blit(font.render(data[i], False, border_color), (width // 2 - width // 10, 100 + count))
        count += 70
    pg.display.flip()
    
#   Settings button

def settings(screen):
    pg.display.set_caption('Settings')
    screen.fill(color)
    create_border(screen)

    #   Menu button
    font = pg.font.Font('8201.ttf', 23)
    data = 'Menu'
    screen.blit(font.render(data, False, color), (width - size_rec * 4, 0))
    pg.draw.rect(screen, (0, 100, 140), (width - size_rec, 0, size_rec, size_rec))

    #   Dark theme


    pg.display.flip()

#   For text on each button

def output_text_menu(screen):
    font = pg.font.Font('8201.ttf', 23)
    data = 'Snake', 'About Us', 'Settings', 'Quit', 'Menu'
    screen.blit(font.render(data[0], False, color), (width // 2 - width // 10 + 20, 100))
    screen.blit(font.render(data[1], False, color), (width // 2 - width // 10 + 5, 170))
    screen.blit(font.render(data[2], False, color), (width // 2 - width // 10 + 15, 243))
    screen.blit(font.render(data[3], False, color), (width // 2 - width // 10 + 28, 313))
    screen.blit(font.render(data[4], False, color), (width - size_rec * 4, 0))

#   Menu

def menu(screen):
    pg.display.set_caption('Menu')
    screen.fill(color)
    create_border(screen)

    #   Menu button
    pg.draw.rect(screen, (0, 100, 140), (width - size_rec, 0, size_rec, size_rec))

    #   Start button
    pg.draw.rect(screen, border_color, (width // 2 - width // 10, 90, 100, 50))

    #   About us
    pg.draw.rect(screen, border_color, (width // 2 - width // 10, 160, 100, 50))

    #   Settings button
    pg.draw.rect(screen, border_color, (width // 2 - width // 10, 230, 100, 50))

    #   Quit button
    pg.draw.rect(screen, border_color, (width // 2 - 50, 300, 100, 50))

    output_text_menu(screen)
    pg.display.flip()
    gameover = False
    is_menu = False
    click = True
    while not gameover:
        for event in pg.event.get():
            print(event)
            if event.type == pg.QUIT:
                gameover = True
            if event.type == pg.MOUSEBUTTONDOWN:
                #   Exit
                if pg.mouse.get_pos()[0] >= width // 2 - width // 10 and pg.mouse.get_pos()[1] >= 300:
                    if pg.mouse.get_pos()[0] <= width // 2 + width // 10 and pg.mouse.get_pos()[1] <= 370:
                        if click is True:
                            click = False
                            sys.exit()
                #   Settings
                elif pg.mouse.get_pos()[0] >= width // 2 - width // 10 and pg.mouse.get_pos()[1] >= 230:
                    if pg.mouse.get_pos()[0] <= width // 2 + width // 10 and pg.mouse.get_pos()[1] <= 280:
                        if click is True:
                            click = False
                            settings(screen)
                #   Info
                elif pg.mouse.get_pos()[0] >= width // 2 - width // 10 and pg.mouse.get_pos()[1] >= 160:
                    if pg.mouse.get_pos()[0] <= width // 2 + width // 10 and pg.mouse.get_pos()[1] <= 210:
                        if click is True:
                            click = False
                            about_us(screen)
                #   Game
                elif pg.mouse.get_pos()[0] >= width // 2 - width // 10 and pg.mouse.get_pos()[1] >= 90:
                    if pg.mouse.get_pos()[0] <= width // 2 + width // 10 and pg.mouse.get_pos()[1] <= 140:
                        if click is True:
                            click = False
                            startGame(screen)
                #   Back to menu
                elif pg.mouse.get_pos()[0] >= width - size_rec and pg.mouse.get_pos()[1] >= 0:
                    if pg.mouse.get_pos()[0] <= width and pg.mouse.get_pos()[1] <= height - size_rec:
                        is_menu = True
                        click = True
                        break
        if is_menu is True:
            break
    if is_menu is True:
        menu(screen)

def main():
    pg.init()
    pg.font.init()
    screen = pg.display.set_mode(size)
    menu(screen)

if __name__ == '__main__':
    main()
