#import pygame   

#pygame.init()   # ALL pygame programs need to initialize the pygame engine
                ## before they can use it

#info =pygame. display.Info()              # including current_w and current_h
#RED = (255, 0, 0)
#WHITE = (255, 255, 255)
#YELLOW = (255, 255, 0)
#SIZE = (info.current_w, info.current_h)                 # sets the width and height of our screen
                                            ## to be the current of each for the monitor  

## pygame.FULLSCREEN in the line below sets pygame to run and use the full screen
#screen = pygame.display.set_mode(SIZE,pygame.FULLSCREEN)
#pygame.display.set_caption('Animation')            # sets the caption on the top left 

## draw our nice background using info settings
#pygame.draw.rect(screen, WHITE, (0,0, info.current_w, info.current_h))

#pygame.draw.rect(screen, YELLOW, (800, 100, 200, 800))
#pygame.draw.circle(screen, YELLOW, (800, 850), 150)
#pygame.draw.circle(screen, YELLOW, (1000, 850), 150)
#pygame.draw.circle(screen, YELLOW, (900, 100), 100)
#pygame.display.flip()   
#pygame.time.wait(1000)
#pygame.quit()

#info.current_w repersents width of the current display utlised.
#info.current_h repersents the height of the current display utilised.

import pygame

pygame.init()
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
SIZE = (1000, 2000)
screen = pygame.display.set_mode(SIZE)
events = pygame.event.get()
x = 150
y = 150
moveX = 0
moveY = 0
moveCount = 0
pygame.draw.rect(screen, WHITE, (0, 0, 1000, 1000))
pygame.draw.circle (screen, YELLOW, (x+moveX, y+moveY), 125, 0)
pygame.draw.circle (screen, BLACK, (x+moveX, y+moveY-40), 10, 0)
pygame.draw.polygon(screen, WHITE, ((x+moveX, y+moveY), (x+moveX+150, y+moveY+100), (x+moveX+150, y+moveY-100)))
pygame.display.flip()

pygame.time.wait (1000)