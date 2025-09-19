# attempt to make a basic idle game with pygame
import pygame as pg
import datetime as dt

###
#GLOBAL VARIABLES
###
# set program frames per second (fps)
fps = 30
# program window dimensions
winY = 400
winX = 800
# defining colors
black = pg.Color(41, 41, 41)
white = pg.Color(222, 222, 222)
red = pg.Color(237, 68, 171)
green = pg.Color(125, 230, 30)
blue = pg.Color(116, 202, 255)

##
#CLASSES / OBJECTS
##
# ui object that the use can press
class button:
    def __init__(self, x1, y1, x2, y2, visible):
        self.visible = False
        


##
#FUNCTIONS
##
# init pygame & basic window
def pgInit():
    #init Window
    pg.init()
    # set up window
    screen = pg.display.set_mode((winX, winY))
    #program caption name
    pg.display.set_caption("Hewwo World :3")
    
    return screen

# update graphics
#todo
def updateGraphics(screen):
    # updating the display
    pg.display.update()
    time.sleep(3)
    screen.fill(white)

#updates game logic when called
#
def updateLogic() :
    print("update on frame " )

# updates the gamestate, called on every program loop 
def pgUpdate(screen):
    updateGraphics(screen)
    updateLogic()
    time.sleep(3)

#render text
def drawTxt (message, colour = black):
    # setting a font object
    font = pg.font.Font(None, 30)
    #print message
    font.render(message, 1, (colour))

##
#MAIN LOOP
# note: this should be the only code that's runnning outside of a function
##

scr = pgInit() #creating screen object

running = True
while running:
    pgUpdate(scr)
    
    #detects window events
    # quits on detection of quit :3
    #   todo: incorporate this into another function
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False


pg.quit()