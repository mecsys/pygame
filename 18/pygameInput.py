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
BLUE = (0, 0, 255)
RED = (255, 0, 0)
YELLOW = (0, 255, 255)

font = pygame.font.SysFont(None, 48)


#pygame.draw.rect(windowSurface, (255,0,0), (textRect.left - 20, textRect.top - 20, textRect.width + 40, textRect.height + 40))

# set up the player and food data structure
RESULT = True
START = True
START2 = True
QUIZ = True
FINAL = False

desafio = []
fichas = []
pre_result = []

def drawText(text, font, surface, x, y,f,b):
    textobj = font.render(text, 1, f, b)
    textrect = textobj.get_rect()    
    textrect.topleft = (x, y)
    return textobj, textrect, text
    print("Retangulo criado!")
#    surface.blit(textobj, textrect)
#18,34

for i in range(7):
#    fichas.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))
    x, y, t = drawText('8', font, windowSurface, windowSurface.get_rect().centerx, 160, GREEN, WHITE )
    fichas.append({'text':x, 'textrect':y, 'num':t})
    print(fichas[0])

    x, y, t = drawText('9', font, windowSurface, 100, 160, YELLOW, WHITE )
    fichas.append({'text':x, 'textrect':y, 'num':t})
    print(fichas[0])

    x, y, t = drawText('1', font, windowSurface, 400, 160, BLUE, WHITE )
    fichas.append({'text':x, 'textrect':y, 'num':t})
    print(fichas[0])

    x, y, t = drawText('3', font, windowSurface, 30, 360, RED, WHITE )
    fichas.append({'text':x, 'textrect':y, 'num':t})
    print(fichas[0])

    x, y, t = drawText('5', font, windowSurface, 150, 360, BLUE, WHITE )
    fichas.append({'text':x, 'textrect':y, 'num':t})
    print(fichas[0])

    x, y, t = drawText('2', font, windowSurface, 320, 360, RED, WHITE )
    fichas.append({'text':x, 'textrect':y, 'num':t})
    print(fichas[0])

    x, y, t = drawText('7', font, windowSurface, 540, 360, GREEN, WHITE )
    fichas.append({'text':x, 'textrect':y, 'num':t})
    print(fichas[0])

    random.shuffle(fichas)
    

def init_screen():
    print("Init_screen funciona!")
    x, y, t = drawText('7', font, windowSurface, (WINDOWWIDTH / 3) - 100, (WINDOWHEIGHT / 3),(0,255,0),(255,255,255))
    desafio.append({'num':t, 'textrect':y})
    windowSurface.blit(x,y)
    pygame.display.update()
    sleep(1)

    x, y, t  = drawText('+', font, windowSurface, (WINDOWWIDTH / 3) - 50, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
    desafio.append({'num':t, 'textrect':y})
    windowSurface.blit(x,y)
    pygame.display.update()
    sleep(1)

    x, y, t = drawText('2', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3),(255,0,0),(255,255,255))
    desafio.append({'num':t, 'textrect':y})
    windowSurface.blit(x,y)
    pygame.display.update()
    sleep(1)    

    x, y, t = drawText('+', font, windowSurface, (WINDOWWIDTH / 3) + 50, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
    desafio.append({'num':t, 'textrect':y})
    windowSurface.blit(x,y)
    pygame.display.update()
    sleep(1)    

    x, y, t = drawText('5', font, windowSurface, (WINDOWWIDTH / 3) + 100, (WINDOWHEIGHT / 3),(0,0,255),(255,255,255))
    desafio.append({'num':t, 'textrect':y})
    windowSurface.blit(x,y)

    x, y, t = drawText('=', font, windowSurface, (WINDOWWIDTH / 3) + 150, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
    desafio.append({'num':t, 'textrect':y})
    windowSurface.blit(x,y)
    pygame.display.update()
    sleep(1)

def init_screen_2():
    print("Init_screen_2 funciona!")
    windowSurface.fill(BLACK)

    x, y, t = drawText('7', font, windowSurface, (WINDOWWIDTH / 3) - 100, (WINDOWHEIGHT / 3),(0,255,0),(255,255,255))
    desafio.append({'num':t, 'textrect':y})
    windowSurface.blit(x,y)
    pygame.display.update()
    

    x, y, t  = drawText('+', font, windowSurface, (WINDOWWIDTH / 3) - 50, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
    desafio.append({'num':t, 'textrect':y})
    windowSurface.blit(x,y)
    pygame.display.update()
   

    x, y, t = drawText('2', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3),(255,0,0),(255,255,255))
    desafio.append({'num':t, 'textrect':y})
    windowSurface.blit(x,y)
    pygame.display.update()
    

    x, y, t = drawText('+', font, windowSurface, (WINDOWWIDTH / 3) + 50, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
    desafio.append({'num':t, 'textrect':y})
    windowSurface.blit(x,y)
    pygame.display.update()
      

    x, y, t = drawText('5', font, windowSurface, (WINDOWWIDTH / 3) + 100, (WINDOWHEIGHT / 3),(0,0,255),(255,255,255))
    desafio.append({'num':t, 'textrect':y})
    windowSurface.blit(x,y)

    x, y, t = drawText('=', font, windowSurface, (WINDOWWIDTH / 3) + 150, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
    desafio.append({'num':t, 'textrect':y})
    windowSurface.blit(x,y)
    pygame.display.update()
    

    #Solução
    x, y, t = drawText('15', font, windowSurface, 150 , 350, BLUE, WHITE)
    desafio.append({'num':t, 'textrect':y})
    pygame.draw.rect(windowSurface, WHITE, (y.left - 10, y.top - 10, y.width + 20, y.height + 20))
    windowSurface.blit(x,y)
    #pygame.display.update()
    
    

    x, y, t = drawText('14', font, windowSurface, 250, 350, YELLOW, WHITE)
    desafio.append({'num':t, 'textrect':y})
    pygame.draw.rect(windowSurface, WHITE, (y.left - 10, y.top - 10, y.width + 20, y.height + 20))
    windowSurface.blit(x,y)
    #pygame.display.update()
    

    x, y, t = drawText('11', font, windowSurface, 350, 350, RED, WHITE)
    desafio.append({'num':t, 'textrect':y})
    pygame.draw.rect(windowSurface, WHITE, (y.left - 10, y.top - 10, y.width + 20, y.height + 20))
    windowSurface.blit(x,y)
    #pygame.display.update()
    



def final():
    global FINAL
    FINAL = True
    init_screen_2()

def test_click(x, y):
    
    if FINAL:
        for cont in desafio:
            if cont['textrect'].collidepoint(x,y):
                aux = int(cont['num'])
                print(aux)

                test = int(pre_result[0])
                test += int(pre_result[1])
                test += int(pre_result[2])
                print(test)

                if aux == test:
                    windowSurface.fill(WHITE)
                    x, y, t = drawText('PARABÉNS VOCÊ GANHOU ;-) !!!', font, windowSurface, windowSurface.get_rect().centerx, 160, BLUE, RED )
                    y.centerx = windowSurface.get_rect().centerx
                    y.centery = windowSurface.get_rect().centery
                    pygame.draw.rect(windowSurface, WHITE, (y.left - 10, y.top - 10, y.width + 20, y.height + 20))
                    windowSurface.blit(x,y)
                    pygame.display.update()
                    sleep(10)
                    sys.exit(0)
                    
                else:
                    windowSurface.fill(RED)
                    x, y, t = drawText('LAMENTO, VOCÊ NÃO GANHOU 8-( !!!', font, windowSurface, windowSurface.get_rect().centerx, 160, WHITE, BLUE )
                    y.centerx = windowSurface.get_rect().centerx
                    y.centery = windowSurface.get_rect().centery
                    pygame.draw.rect(windowSurface, WHITE, (y.left - 10, y.top - 10, y.width + 20, y.height + 20))
                    windowSurface.blit(x,y)
                    pygame.display.update()
                    sleep(10)
                    sys.exit(0)

    for cont in fichas:       
        if cont['textrect'].collidepoint(x,y):
            print("VC ACERTOU O RETANGULO!!! =>", cont['num'])
            pre_result.append(cont['num'])
            print(pre_result)
            if len(pre_result) == 3:
                global QUIZ
                QUIZ = False
                final()
            break
            
def quiz():
      
    for x in fichas:       
#        windowSurface.blit(x['text'],x['textrect'])
        pygame.draw.rect(windowSurface, WHITE, (x['textrect'].left - 10, x['textrect'].top - 10, x['textrect'].width + 20, x['textrect'].height + 20))
        windowSurface.blit(x['text'], x['textrect'])
   

#    if RESULT:
#        print("Mouse moveu!")
#        global QUIZ
#        QUIZ = True

# run the game loop
while True:
    # check for events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
#        if event.type == MOUSEBUTTONDOWN:
        if event.type == MOUSEBUTTONUP:
            print("Mouse call!")
            #foods.append(pygame.Rect(event.pos[0], event.pos[1], FOODSIZE, FOODSIZE))            
            #pass
            test_click(event.pos[0], event.pos[1])            
            
    
    # draw the black background onto the surface
    windowSurface.fill(BLACK)

    # draw the player onto the surface
    if START:
        init_screen()
        START = False
    
    if QUIZ:
        quiz()        

    if FINAL:
        final()
   
    # draw the window onto the screen
    pygame.display.update()
    mainClock.tick(40)
