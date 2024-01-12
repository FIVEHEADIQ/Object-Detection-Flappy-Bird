import sys
import pygame
from pygame.locals import QUIT
import os

class Movement:
  def __init__(self, width, height):
    # Set up initial coordinates
    self.x, self.y = width // 5, height // 2.5

    # Set up the speed of movement
    self.speed = 5

  # Main game loop
  def flappyBird(self, screen):
    # Get the state of all keys
    keys = pygame.key.get_pressed()

    # Update coordinates based on key presses
    if keys[pygame.K_UP]:
        self.y -= self.speed
    if keys[pygame.K_DOWN]:
        self.y += self.speed

    # Draw a circle at the current coordinates
    pygame.draw.circle(screen, (0, 0, 6), (self.x, self.y), 15)
