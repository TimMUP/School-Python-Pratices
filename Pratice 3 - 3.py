
#import pygame   
#pygame.init()
#WHITE = (255,255,255)
#RED = (255, 0, 0)
#BLACK = (0,0,0)
#SIZE = (800, 800)
#screen = pygame.display.set_mode(SIZE)
#screen.fill(WHITE)
#pygame.draw.line(screen, BLACK, (100,100), (700,100),5)  # Mouth
#pygame.draw.line(screen, BLACK, (100,700), (100,100),5)  # Mouth
#pygame.draw.line(screen, BLACK, (700,700), (700,100),5)  # Mouth
#pygame.draw.line(screen, BLACK, (700,700), (100,700),5)  # Mouth

#pygame.draw.line(screen, BLACK, (100,300), (700,300),5)  # Mouth
#pygame.draw.line(screen, BLACK, (100,500), (700,500),5)  # Mouth

#pygame.draw.line(screen, BLACK, (300,100), (300,700),5)
#pygame.draw.line(screen, BLACK, (500,100), (500,700),5)

#pygame.display.flip()
#pygame.time.wait(3000)
#pygame.quit()


#import pygame

#locationX = int(input("Please enter the X-Coordinate of your 3D Box:"))
#locationY = int(input("Please enter the Y-Coordinate of your 3D Box:"))
#locationX = locationX+100*10
#locationY = locationY*10

#pygame.init()
#WHITE = (255,255,255)
#RED = (255, 0, 0)
#BLACK = (0,0,0)
#SIZE = (800, 800)
#screen = pygame.display.set_mode(SIZE)
#screen.fill(WHITE)
#x = 0
#y = 0
#while x <=800:
    #pygame.display.flip()
    #pygame.draw.line(screen, BLACK, (x, 0), (x, 800), 1)
    #x = x + 100
#while y <=800:
    #pygame.display.flip()
    #pygame.draw.line(screen, BLACK, (0, y), (800, y), 1)
    #y = y + 100
    
#pygame.display.flip()
#pygame.draw.line(screen, BLACK, (locationX, locationY+100), (locationX, locationY+300), 10)
#pygame.draw.line(screen, BLACK, (locationX+200, locationY+100), (locationX+200, locationY+300), 10)
#pygame.draw.line(screen, BLACK, (locationX, locationY+100), (locationX+200, locationY+100), 10)
#pygame.draw.line(screen, BLACK, (locationX, locationY+300), (locationX+200, locationY+300), 10)
#pygame.draw.line(screen, BLACK, (locationX, locationY+100), (locationX+100, locationY), 10)
#pygame.draw.line(screen, BLACK, (locationX+100, locationY), (locationX+300, locationY), 10)
#pygame.draw.line(screen, BLACK, (locationX+200, locationY+100), (locationX+300, locationY), 10)
#pygame.draw.line(screen, BLACK, (locationX+300, locationY), (locationX+300, locationY+200), 10)
#pygame.draw.line(screen, BLACK, (locationX+200, locationY+300), (locationX+300, locationY+200), 10)
#pygame.display.flip()

#pygame.time.wait(4000)
#pygame.quit()

