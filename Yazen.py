import sys
import pygame
from pygame.locals import QUIT
import os
import jack
pygame.init()
DISPLAYSURF = pygame.display.set_mode((720, 480))

image_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')  
background_path = os.path.join(image_folder, 'ground.jpg')
#background.jpg  # Replace with your actual image path
background = pygame.image.load(background_path).convert()
background = pygame.transform.smoothscale(background, DISPLAYSURF.get_size())
bg_width = background.get_width()
x_pos = 0
clock = pygame.time.Clock()
jack = jack.Movement(720,480)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Blit the background image
    DISPLAYSURF.blit(background, (x_pos, 0))
    DISPLAYSURF.blit(background, (x_pos + bg_width,0))

    x_pos -= 1

    if x_pos < -bg_width:
        x_pos = 0  

    # Add other game elements (sprites, text, etc.) here
    jack.flappyBird(DISPLAYSURF)


  
    pygame.display.update()

    clock.tick(80)
