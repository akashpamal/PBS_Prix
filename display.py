import pygame as pg
import numpy as np

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 800

BLACK = (0, 0, 0)
GRASS_GREEN = (106, 140, 76)

RACECAR = pg.image.load('./assets/OrangeCar.png')

def quitGame(): #Quits Pygame and Python
    pg.quit()
    quit()
    
def backgroundInputCheck(eventList): #Constantly checks for quits and enters
    for event in eventList:
            if event.type == pg.QUIT:
                quitGame()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    quitGame()
                    
def runGame():
    
    print("HI")
    while True:
        deltaTime = clock.get_time()
        backgroundInputCheck(pg.event.get())
        
        print("Pi")
        #tick racecar
        screen.fill(GRASS_GREEN)
        
        #draw car
        #screen.blit(RACECAR, (0, 0))
        
        clock.tick(60)
        pg.display.flip()
    
def draw_track():
    gameDisplay = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    




if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pg.display.set_caption("PBS Prix")
    clock = pg.time.Clock()
    runGame()