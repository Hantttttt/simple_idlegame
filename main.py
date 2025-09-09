# attempt to make a basic idle game with pygame
import pygame as pg
import time

###
#GLOBAL VARIABLES
###
# program window dimensions
winY = 400
winX = 800
# defining colors
black = pg.Color(41, 41, 41)
white = pg.Color(222, 222, 222)
red = pg.Color(237, 68, 171)
green = pg.Color(125, 230, 30)
blue = pg.Color(116, 202, 255)

#initialize pygame
pg.init()

# set up window
screen = pg.display.set_mode((winX, winY))
#program caption name
pg.display.set_caption("Hewwo World :3")

##
#FUNCTIONS
##




##
#MAIN LOOP
##

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


pg.quit()