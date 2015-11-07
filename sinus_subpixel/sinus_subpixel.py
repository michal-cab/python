DOTS = 100

import pygame
from pygame.locals import *

from subpixelsurface import *

from math import sin, cos

def run():
    
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    #screen = pygame.display.set_mode((640, 480),FULLSCREEN)
    clock = pygame.time.Clock()
    dot = pygame.image.load("dot.png")    
    dot_subpixel = SubPixelSurface(dot, x_level=8)    
        
    t = 0.
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        
        time_passed = clock.tick()
        t+= time_passed / 3000.


        for n in xrange(DOTS):
            a = float(n)/DOTS * sin((t)*.1234)*100
            x = sin((t+a)*sin(t/4)) * 200.*sin(t/5) + 320
            y = cos(((t*1.234)+a)*sin(t/8)) * 200.*sin(t/4) + 220
            screen.blit(dot_subpixel.at(x,y), (x, y))
        pygame.display.update() 

run()
