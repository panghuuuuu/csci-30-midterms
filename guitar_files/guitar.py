#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import sys
import pygame

if __name__ == '__main__':
    pygame.init()
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))

    keyboard = ["q","2","w","e","4","r","5","t","y","7","u","8","i","9","o","p"]
    string = list()
    for i in range(16):
        x = 440*(1.059463**(i-12))
        string.append(GuitarString(x))
    sample = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                key = event.unicode
                if key in keyboard: 
                    x = keyboard.index(key)
                    string[x].pluck()
                else:
                    pass

        for i in range(16):
            sample += string[i].sample()
        play_sample(sample)

        for i in range(16):
            string[i].tick()
