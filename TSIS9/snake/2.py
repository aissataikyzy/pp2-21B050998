from dataclasses import dataclass
import pygame, sys
import random
import time
import datetime

#_____General Variables for use in the program_____
HEIGHT = 400
WIDTH = 400
SCORE = 0
BLOCK_SIZE = 20

#_____Creating colors_____
RED   = (255, 0, 0)
RED2  = (200, 0, 0)
GREEN = (0, 255, 0)
BLUE  = (0, 0, 255)
BLACK = (0, 0, 0)
PURPLE = (255, 0, 255)
WHITE = (255, 255, 255)


#_____Initializing all Classes_____
class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

class Food:
    def __init__(self):
        self.location = Point(random.randint(0, WIDTH/BLOCK_SIZE - 1), random.randint(0, HEIGHT/BLOCK_SIZE - 1))
        self.x = self.location.x
        self.y = self.location.y
        self.current = random.randint(0, 2)
        self.values = [1, 2, 5]
        self.colors = [GREEN, BLUE, PURPLE]

    def draw(self):
        point = self.location
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, self.colors[self.current], rect)


class Snake:
    def __init__(self):
        self.body = [Point(10, 11)]
        self.dx = 1
        self.dy = 0

    def move(self):    
        for i in range(len(self.body) - 1, 0, -1):
            self.body[i].x = self.body[i-1].x
            self.body[i].y = self.body[i-1].y

        self.body[0].x += self.dx 
        self.body[0].y += self.dy 

        if self.body[0].x * BLOCK_SIZE > WIDTH:
            self.body[0].x = 0
        
        if self.body[0].y * BLOCK_SIZE > HEIGHT:
            self.body[0].y = 0

        if self.body[0].x < 0:
            self.body[0].x = WIDTH / BLOCK_SIZE
        
        if self.body[0].y < 0:
            self.body[0].y = HEIGHT / BLOCK_SIZE

    def draw(self):
        point = self.body[0]
        rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
        pygame.draw.rect(SCREEN, RED, rect)


        for point in self.body[1:]:
            rect = pygame.Rect(BLOCK_SIZE * point.x, BLOCK_SIZE * point.y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, RED2, rect)

    def check_collision(self, entity):
        if self.body[0].x == entity.x:
            if self.body[0].y == entity.y:
                return True
        return False



#_____Main program_____
def main():
    global SCREEN, CLOCK

    #_____Pygame initialing_____
    pygame.init()

    #_____Other Variables for use in the program_____
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
    CLOCK = pygame.time.Clock()
    FOOD_EATED = False    # Need to avoid death from eating food
    SPEED = 0
    SCREEN.fill(BLACK)
    timer = datetime.datetime.now()
    font = pygame.font.SysFont("Verdana", 15)

    #_____Creating snake and food entities_____
    snake = Snake()
    food = Food()


    #_____Game Loop_____
    while True:

        #_____Cycles through all events occuring_____
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if snake.dy == 0: continue
                    snake.dx = 1
                    snake.dy = 0
                if event.key == pygame.K_LEFT:
                    if snake.dy == 0: continue
                    snake.dx = -1
                    snake.dy = 0
                if event.key == pygame.K_UP:
                    if snake.dx == 0: continue
                    snake.dx = 0
                    snake.dy = -1
                if event.key == pygame.K_DOWN:
                    if snake.dx == 0: continue
                    snake.dx = 0
                    snake.dy = 1


        snake.move()

        #_____Check collision between snake and food_____
        if snake.check_collision(food):
            global SCORE
            FOOD_EATED = True
            SCORE += food.values[food.current]
            snake.body.append(Point(food.location.x, food.location.y))

            #_____Level(SPEED) incresing_____
            if (len(snake.body) % 3 == 0 and len(snake.body) != 0): 
                SPEED += 2

            #_____New place to food_____
            food.location = Point(random.randint(0, WIDTH/BLOCK_SIZE - 1), random.randint(0, HEIGHT/BLOCK_SIZE - 1))
            food.x = food.location.x
            food.y = food.location.y
            food.current = random.randint(0, 2)

            timer = datetime.datetime.now()
            

            
        #_____Check collision between Snake and Snake Body_____
        for cell in snake.body[1:]:
            if snake.check_collision(cell):
                if FOOD_EATED: continue
                time.sleep(2)
                pygame.quit()
                sys.exit()


        #_____Score and Level rendering_____
        SCREEN.fill(BLACK)
        scores = font.render('Score: ' + str(SCORE), True, WHITE)
        SCREEN.blit(scores, (10,8))
        scores = font.render('Level: ' + str(SPEED / 2)[0:1], True, WHITE)
        SCREEN.blit(scores, (10,25))

        FOOD_EATED = False

        snake.draw()
        food.draw()
        
        #_____Food timer_____
        delta = datetime.datetime.now() - timer

        if delta.total_seconds() > 10:
            food.location = Point(random.randint(0, WIDTH/BLOCK_SIZE - 1), random.randint(0, HEIGHT/BLOCK_SIZE - 1))
            food.x = food.location.x
            food.y = food.location.y
            food.current = random.randint(0, 2)
            timer = datetime.datetime.now()


        pygame.display.update()
        #_____Need to increase Snakes Speed_____
        CLOCK.tick(6 + SPEED)


#_____main program start_____
main()