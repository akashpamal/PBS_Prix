import pygame as pg
import numpy as np
from car import Car

SCREEN_WIDTH = 1440
SCREEN_HEIGHT = 800

BLACK = (0, 0, 0)
GRASS_GREEN = (106, 140, 76)
RACECAR = pg.image.load('./assets/OrangeCar.png')

VERT_TRACK = pg.image.load('./assets/VerticalTrack.jpeg')
HOR_TRACK = pg.image.load('./assets/HorizontalTrack.jpeg')
LEFT_TURN = pg.image.load('./assets/LeftTurn.jpeg')
RIGHT_TURN = pg.image.load('./assets/RightTurn.jpeg')
FINISH_LINE = pg.image.load('./assets/FinishLine.jpeg')

TRACK_1 = pg.image.load('./assets/Track1.jpeg')
TRACK_1 = pg.transform.scale(TRACK_1, (16000, 8000))

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
                    
def main():
    playerCar = Car(RACECAR, 6800, 2300)
    
    while True:
        deltaTime = clock.get_time()
        backgroundInputCheck(pg.event.get())
        
        playerCar.getInput(pg.key.get_pressed(), deltaTime)
        playerCar.update(deltaTime)
        
        #tick racecar
        screen.fill(GRASS_GREEN)
        screen.blit(TRACK_1, (-playerCar.position.x, -playerCar.position.y))
        playerCar.draw(screen, SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
         
        clock.tick(60)
        pg.display.flip()
    
    
if __name__ == "__main__":
    pg.init()
    screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
    pg.display.set_caption("PBS Prix")
    clock = pg.time.Clock()
    main()