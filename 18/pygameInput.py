#!/usr/bin/env python
import pygame, sys, random
from pygame.locals import *

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()

# set up the window
<<<<<<< HEAD
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), \
pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.FULLSCREEN, 32)
=======
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
>>>>>>> 6a3969eebf0b1ea1e163fd782cede3cfa8a75dcb
pygame.display.set_caption('Input')

# set up the colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# set up the player and food data structure
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
player = pygame.Rect(300, 100, 50, 50)
foods = []
for i in range(20):
    foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

# set up movement variables
moveLeft = False
moveRight = False
moveUp = False
moveDown = False

MOVESPEED = 6


# run the game loop
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            # change the keyboard variables
            if event.key == K_LEFT or event.key == ord('a') or event.key == K_KP4:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == ord('d') or event.key == K_KP6:
                moveLeft = False
                moveRight = True
            if event.key == K_UP or event.key == ord('w') or event.key == K_KP8:
                moveDown = False
                moveUp = True
            if event.key == K_DOWN or event.key == ord('s') or event.key == K_KP2:
                moveUp = False
                moveDown = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == ord('a'): or event.key == K_KP4:
                moveLeft = False
            if event.key == K_RIGHT or event.key == ord('d') or event.key == K_KP6:
                moveRight = False
            if event.key == K_UP or event.key == ord('w') or event.key == K_KP8:
                moveUp = False
            if event.key == K_DOWN or event.key == ord('s') or event.key == K_KP2:
                moveDown = False
            if event.key == ord('x'):
                player.top = random.randint(0, WINDOWHEIGHT - player.height)
                player.left = random.randint(0, WINDOWWIDTH - player.width)

        if event.type == MOUSEBUTTONUP:
            foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))

    foodCounter += 1
    if foodCounter >= NEWFOOD:
        # add new food
        foodCounter = 0
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    # draw the black background onto the surface
    windowSurface.fill(BLACK)

    # move the player
    if moveDown and player.bottom < WINDOWHEIGHT:
        player.top += MOVESPEED
    if moveUp and player.top > 0:
        player.top -= MOVESPEED
    if moveLeft and player.left > 0:
        player.left -= MOVESPEED
    if moveRight and player.right < WINDOWWIDTH:
        player.right += MOVESPEED

    # draw the player onto the surface
    pygame.draw.rect(windowSurface, WHITE, player)

    # check if the player has intersected with any food squares.
    for food in foods[:]:
        if player.colliderect(food):
            foods.remove(food)

    # draw the food
    for i in range(len(foods)):
        pygame.draw.rect(windowSurface, GREEN, foods[i])

    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)