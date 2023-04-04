import pygame, sys

from pygame.locals import *

pygame.init()







#colors

BLACK = (0, 0, 0)

WHITE = (255, 255, 255)

RED = (255, 0, 0) 

GREEN = (0, 255, 0)

BLUE = (0, 0, 255)

GREY = (128, 128, 128)

WIDTH = 600

HEIGHT = 600




screen = pygame.display.set_mode((600, 600))

clock = pygame.time.Clock()

FPS = 30

pygame.display.set_caption("simple paint")




start = None

move = None

position = None

action = 'drawing'

color = BLACK

screen.fill(WHITE)




done = False

while not done:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            done = True

        if event.type == pygame.KEYDOWN:

            #выбрать фигуры

            if event.key == pygame.K_r:

                action = 'rectangle'

            if event.key == pygame.K_c:

                action = 'circle'

            if event.key == pygame.K_d:

                action = 'drawing' 

            if event.key == pygame.K_e:

                action = 'erase'        

            #выбрать цвета     

            if event.key == pygame.K_1:

                color = RED

            if event.key == pygame.K_2:

                color = GREEN

            if event.key == pygame.K_3:

                color = BLUE

            if event.key == pygame.K_4:

                color = GREY

            if event.key == pygame.K_5:

                color = BLACK 

    #drawing lines                        

    if action == 'drawing':

        if event.type == pygame.MOUSEBUTTONDOWN:

            start = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEMOTION:

            move = pygame.mouse.get_pos()

        if start: #рисуем на экране

            pygame.draw.line(screen, color, start, move, 2)  

            start = move 

        if event.type == pygame.MOUSEBUTTONUP:

            start = None #прекращаем рисовать

    #erase        

    if action == 'erase':

        if event.type == pygame.MOUSEBUTTONDOWN:

            start = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEMOTION:

            move = pygame.mouse.get_pos()  

        if start:

            pygame.draw.line(screen, WHITE, start, move, 10)

            start = move

        if event.type == pygame.MOUSEBUTTONUP:

            start = None

    #drawing circle        

    if action == 'circle':

        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y =pygame.mouse.get_pos() 

            position = 'd'

        if event.type == pygame.MOUSEBUTTONUP: 

            x1, y1 =pygame.mouse.get_pos()

            position = 'u'

        if position == 'u':

            r = ((x-x1)**2+(y-y1)**2)**0.5 #formula 

            pygame.draw.circle(screen, color, (x,y), r, 2)

            position = None        

    #drawing rectangle

    if action == 'rectangle':

        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y =pygame.mouse.get_pos() 

            position = 'd'

        if event.type == pygame.MOUSEBUTTONUP:

            x1, y1 =pygame.mouse.get_pos() 

            position = 'u'

        if position == 'u':

            if x < x1 and y < y1: 

                pygame.draw.rect(screen,color,((x,y,x1-x,y1-y)),2) 

            elif x < x1 and y > y1:

                pygame.draw.rect(screen,color, (x,y1,x1-x,y-y1),2) 

            elif x > x1 and y > y1:

                pygame.draw.rect(screen,color,(x1,y1,x-x1,y-y1),2) 

            else:

                pygame.draw.rect(screen,color,(x1,y,x-x1,y1-y),2) 

            position =None

    #drawing square

    if action == 'square':

        if event.type == pygame.MOUSEBUTTONDOWN:

            x, y =pygame.mouse.get_pos() 

            position = 'd'

        if event.type == pygame.MOUSEBUTTONUP:

            x1, y1 =pygame.mouse.get_pos() 

            position = 'u'

        if position == 'u':

            if x < x1 and y < y1:# формулы

                if x1-x>y1-y: 

                    pygame.draw.rect(screen,color,((x,y,x1-x,x1-x)),2)

                else:

                    pygame.draw.rect(screen,color,((x,y,y1-y,y1-y)),2)
            elif x < x1 and y > y1:

                if x1-x>y-y1:

                    pygame.draw.rect(screen,color,((x,y1,x1-x,x1-x)),2)

                else:

                    pygame.draw.rect(screen,color,((x,y1,y-y1,y-y1)),2)

            elif x > x1 and y > y1:

                if x-x1>y-y1:

                    pygame.draw.rect(screen,color,(x1,y1,x-x1,x-x1),2)

                else:

                    pygame.draw.rect(screen,color,(x1,y1,y-y1,y-y1),2)

            else:

                if x-x1 > y1-y:

                    pygame.draw.rect(screen,color,(x1,y,x-x1,x-x1),2)

                else:

                    pygame.draw.rect(screen,color,(x1,y,y1-y,y1-y),2)

            position =None

    pygame.display.flip()

    clock.tick(FPS)        







pygame.quit()

#Give feedback    
                    