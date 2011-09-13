import pygame, sys, random
from time import sleep
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


#pygame.draw.rect(windowSurface, (255,0,0), (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# set up the player and food data structure
RESULT = False
START = True
START2 = True
QUIZ = True
fichas = []

def drawText(text, font, surface, x, y,f,b):
    textobj = font.render(text, 1, f, b)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    return textobj, textrect
#    surface.blit(textobj, textrect)

for i in range(7):
#    fichas.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
    x, y = drawText(str(random.randint(0, 10)), font, windowSurface, random.randint(0, WINDOWWIDTH), random.randint(0, WINDOWHEIGHT), GREEN, WHITE )
    fichas.append({'text':x, 'textrect':y})


def init_screen():
    print("Init_screen funciona!")
    x, y = drawText('10', font, windowSurface, (WINDOWWIDTH / 3) - 100, (WINDOWHEIGHT / 3),(0,255,0),(255,255,255))
    windowSurface.blit(x,y)
    pygame.display.update()
    sleep(1)

    x, y = drawText('+', font, windowSurface, (WINDOWWIDTH / 3) - 50, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
    windowSurface.blit(x,y)
    pygame.display.update()
    sleep(1)

    x, y = drawText('20', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3),(255,0,0),(255,255,255))
    windowSurface.blit(x,y)
    pygame.display.update()
    sleep(1)    

    x, y = drawText('+', font, windowSurface, (WINDOWWIDTH / 3) + 50, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
    windowSurface.blit(x,y)
    pygame.display.update()
    sleep(1)    

    x, y = drawText('30', font, windowSurface, (WINDOWWIDTH / 3) + 100, (WINDOWHEIGHT / 3),(0,0,255),(255,255,255))
    windowSurface.blit(x,y)

    x, y = drawText('=', font, windowSurface, (WINDOWWIDTH / 3) + 150, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
    windowSurface.blit(x,y)
    pygame.display.update()
    sleep(6)
    
    
    #pygame.draw.rect(windowSurface, WHITE, player)

def atualiza_screen():
    print("Atualiza_screen funciona!")
    x, y = drawText('10', font, windowSurface, (WINDOWWIDTH / 3) - 100, (WINDOWHEIGHT / 3),(0,255,0),(255,255,255))
    windowSurface.blit(x,y) 
    x, y = drawText('+', font, windowSurface, (WINDOWWIDTH / 3) - 50, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
    windowSurface.blit(x,y)
    x, y = drawText('20', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3),(255,0,0),(255,255,255))
    windowSurface.blit(x,y)
    x, y = drawText('+', font, windowSurface, (WINDOWWIDTH / 3) + 50, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
    windowSurface.blit(x,y)
    x, y = drawText('30', font, windowSurface, (WINDOWWIDTH / 3) + 100, (WINDOWHEIGHT / 3),(0,0,255),(255,255,255))
    windowSurface.blit(x,y)
    x, y = drawText('=', font, windowSurface, (WINDOWWIDTH / 3) + 150, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
    windowSurface.blit(x,y)

def quiz():
    print("Quiz funciona!")
    for x in fichas:
        windowSurface.blit(x['text'],x['textrect'])
        print(x['text'], x['textrect'])

    if RESULT:
        print("Mouse moveu!")
        global QUIZ
        QUIZ = False

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
    if START:
        init_screen()
        START = False
    
    if QUIZ:
        quiz()
    
    if START2:
        print("")
        init_screen()
        START2 = False

    if not QUIZ and START2:
        atualiza_screen()
   
    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)
