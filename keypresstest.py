import pygame
import sys

teamOccupying = 0
pygame.init()
screen = pygame.display.set_mode()
offSet = 50
rectWidth, rectHeight = (300, 300)
team1Color = (0, 255, 255)
team2Color = (0, 0, 255)
screen.fill([255, 0, 0])
width = screen.get_width()
height = screen.get_height()
team1Pos = (height/2, width/2)
team2Pos = (height/2 + offSet, width/2 + offSet)
pygame.draw.rect(screen, team1Color, (team1Pos[1] - rectWidth/2,team1Pos[0] - rectHeight/2, 300, 300))
pygame.draw.rect(screen, team2Color, (team2Pos[1] - rectWidth/2,team2Pos[0] - rectHeight/2, 300, 300))

gameOver = False
while not gameOver:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP1:
                sys.stdout.write(1)
                screen.fill([255, 0, 0])
            if event.key == pygame.K_KP2:
                teamOccupying = 2
                screen.fill([0, 255, 0])
            if event.key == pygame.K_KP3:
                teamOccupying = 2
                screen.fill([0, 255, 0])
            if event.key == pygame.K_BACKSPACE:
                gameOver = True
    pygame.display.update()

#def changeAnimation():
