#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from subpixelsurface import *
from math import sin, cos
import random

def colorize(image, switch):
    image = image.copy()
    if switch == 0:
        image.fill((255,255,255,255),None,pygame.BLEND_RGBA_MULT)
    if switch == 1:
        color1 = random.randint(0,100)
        image.fill((color1,color1,color1,10),None,pygame.BLEND_RGBA_ADD)
    return image

def run():
    loop = True
    dots = 100
    switch = 0
    pause = 1
    t = 0.
    time_factor = 1 

    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    while loop:
        for event in pygame.event.get():
            if event.type == QUIT:
                loop = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    loop = False
                if event.key == K_UP:
                    dots += 10
                if event.key == K_DOWN:
                    dots -= 10
                if event.key == K_LEFT:
                    time_factor -= .1
                if event.key == K_RIGHT:
                    time_factor += .1
                if event.key == K_c:
                    switch = (switch + 1) % 2
                if event.key == K_SPACE:
                    pause = (pause + 1) % 2

        time_passed = clock.tick()
        dot = pygame.image.load("dot.png")
        colorized_dot = colorize(dot, switch)
        dot_subpixel = SubPixelSurface(colorized_dot, x_level=4)
        t += time_factor * (time_passed / 3000.) * pause
        
        for n in range(dots):
            a = float(n)/dots * sin((t)*.1234)*100
            x = sin((t+a)*sin(t/4)) * 200.*sin(t/5) + 320
            y = sin(((t*1.234)+a)*sin(t/8)) * 200.*sin(t/4) + 220
            screen.blit(dot_subpixel.at(x, y), (x, y))
        pygame.display.update()

if __name__ == "__main__":
    run()
    pygame.quit()
