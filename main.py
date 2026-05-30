#pygame.transform.scale(rocket,(200,400))
import pygame
from pygame.locals import *
from time import *
screen = pygame.display.set_mode((600,600))
player_x = 200
player_y = 200
keys = [False,False,False,False]

player = pygame.image.load("RocketInSpace/rocket.png")
background = pygame.image.load("RocketInSpace\spacebg.png")

while player_y < 800:
    screen.blit(background,(0,0))
    screen.blit(player,(player_x, player_y))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit()
            # or pygame.quit()
        if event.type == pygame.KEYDOWN:# checking if any key is pressed
            if event.key == K_UP:
                keys[0]=True
            elif event.key == K_LEFT:
                keys[1]=True
            elif event.key == K_DOWN:
                keys[2]=True
            elif event.key == K_RIGHT:
                keys[3]=True
        #check if keyboard key is released
        if event.type == pygame.KEYUP:
            if event.key == K_UP:
                keys[0]=False
            elif event.key == K_LEFT:
                keys[1]=False
            elif event.key == K_DOWN:
                keys[2]=False
            elif event.key == K_RIGHT:
                keys[3]=False
    if keys[0]:
        if player_y > 0:
            player_y -= 20
    elif keys[2]:
        if player_y < 580:
            player_y += 10

    if keys[1]:
        if player_x > 0:
            player_x -= 10
    elif keys[3]:
        if player_x < 580:
            player_x += 10


    player_y+=10
    pygame.display.update()
    sleep(0.2)
print("Game Over")
