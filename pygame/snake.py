#!/usr/bin/env python3
# petit jeu de snake pour m entrainer un peu

import pygame
import sys, random

pygame.init()
screen = pygame.display.set_mode((600,600))
clock = pygame.time.Clock()

# colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
niceBlack = (0,0,10)
pink = (255,200,200)

# starting direction 
direction = 0
speed = 10
x, y = 12.5, 12.5

#algorithm patterns
snake_x, snake_y = 25, 25
food_in_game = False
food_x = 0
food_y = 0
food_count = 0

def makeFood():
    pygame.draw.rect(screen, green, (food_x, food_y, 25, 25))



while (True):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = 1
            elif event.key == pygame.K_DOWN:
                direction = 0
            elif event.key == pygame.K_RIGHT:
                direction = 3
            elif event.key == pygame.K_LEFT:
                direction = 2
    #fps and movement
    msElapsed = clock.tick(20)
    if direction == 0:
        y = y + 12.5
    elif direction == 1:
        y = y - 12.5
    elif direction == 3:
        x = x + 12.5
    elif direction == 2:
        x = x - 12.5
    # managing the borders
    if x > 575:
        x = 575
    elif x < 0:
        x = 0
    elif y > 575:
        y = 575
    elif y < 0:
        y = 0
    screen.fill(niceBlack)
    # food placement and food eating
    makeFood()
    if food_in_game is False:
        food_y = random.randint(0, 575)
        food_x = random.randint(0, 575)
        food_in_game = True
    if abs(x - food_x) <=snake_x:
        if abs(y - food_y) <=snake_y:
            food_in_game = False
            food_count += 1
            if food_count >= 1:
                snake_x, snake_y = snake_x + (food_count*2), snake_y + (food_count*2)
    pygame.draw.rect(screen, white, (x,y,snake_x, snake_y))
    if food_in_game is False:
        pygame.draw.rect(screen, white, (x,y,snake_x*2,snake_y*2))
    pygame.display.update() 





