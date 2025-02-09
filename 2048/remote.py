import pygame
import serial


pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Joystick")
player_x = 50
player_y = 50

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -=15
            if event.key == pygame.K_RIGHT:
                player_x +=15
            if event.key == pygame.K_UP:
                player_y -=15
            if event.key == pygame.K_DOWN:
                player_y +=15
                
    pygame.display.update()
        
                
                
    