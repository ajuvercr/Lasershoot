import pygame
import sys

teamOccupying = 0
pygame.init()
screen = pygame.display.set_mode()     
screen.fill([255, 0, 0])
pygame.display.update()
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP1:
                sys.stdout.write(1)
                screen.fill([255, 0, 0])
                pygame.display.update()
            if event.key == pygame.K_KP2:
                sys.stdout.write(2)
                screen.fill([0, 255, 0])
                pygame.display.update()                  