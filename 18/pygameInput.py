#!/usr/bin/env python
import pygame, sys, random
from pygame.locals import *

# set up pygame
pygame.init()
mainClock = pygame.time.Clock()
pygame.mouse.set_visible(True)

# set up the window
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Matematica Legal')

# set up the colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

font = pygame.font.SysFont(None, 48)
player = pygame.Rect(300, 100, 150, 150)

# set up the text
text = font.render('10', True, (0,255,0), (0,0,255))
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery


#pygame.draw.rect(windowSurface, (255,0,0), (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

windowSurface.blit(text, textRect)

pygame.draw.rect(windowSurface, WHITE, player)
pygame.display.update()

# set up the player and food data structure
foodCounter = 0
NEWFOOD = 40
FOODSIZE = 20
RESULT = False

def drawText(text, font, surface, x, y,f,b):
    textobj = font.render(text, 1, f, b)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# run the game loop
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == MOUSEBUTTONDOWN:
            #foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))
            RESULT = True
            pass
    
    # draw the black background onto the surface
    windowSurface.fill(BLACK)

    # draw the player onto the surface
    drawText('10', font, windowSurface, (WINDOWWIDTH / 3) - 100, (WINDOWHEIGHT / 3),(0,255,0),(255,255,255))
    drawText('+', font, windowSurface, (WINDOWWIDTH / 3) - 50, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
    drawText('20', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3),(255,0,0),(255,255,255))
    drawText('+', font, windowSurface, (WINDOWWIDTH / 3) + 50, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
    drawText('30', font, windowSurface, (WINDOWWIDTH / 3) + 100, (WINDOWHEIGHT / 3),(0,0,255),(255,255,255))
    drawText('=', font, windowSurface, (WINDOWWIDTH / 3) + 150, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
    if RESULT:
        print("Mouse moveu!")
        drawText('60', font, windowSurface, (WINDOWWIDTH / 3) + 200, (WINDOWHEIGHT / 3),(0,255,255),(0,0,0))
    #pygame.draw.rect(windowSurface, WHITE, player)

   
    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)
