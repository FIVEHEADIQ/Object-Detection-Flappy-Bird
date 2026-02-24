"""
Module for initializing game window and handling user input for quitting the game.
"""
import pygame
from pygame.locals import QUIT
class Skins:
  """
  Initializes the display surface and sets up the paths for image assets
  DISPLAYSURF: the display surface for rendering everything
  """
  def __init__(self, DISPLAYSURF: pygame.surface.Surface):
    import os
    self.DISPLAYSURF = DISPLAYSURF
    # Get absolute path to background.jpg in the same directory as this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    background_path = os.path.join(script_dir, 'background.jpg')
    self.background = pygame.image.load(background_path).convert()
    self.background = pygame.transform.smoothscale(self.background, self.DISPLAYSURF.get_size())
    self.bg_width = self.background.get_width()
    self.x_pos = 0
    self.bird_list = ['flappy bird mans/Blue Man.png', 'flappy bird mans/Green Hat Man.png', 'flappy bird mans/Pink Man.png', 'flappy bird mans/Pixel Blue Man', 'flappy bird mans/Pixel Yellow Man.png', 'flappy bird mans/Yellow Hat Man.png']

  def get_bird_list(self):
     return self.bird_list

  def display_background(self):
    """
    Display the background image on the display surface in a shifting pattern.
    """
      # Blit the self.background image
    self.DISPLAYSURF.blit(self.background, (self.x_pos, 0))
    self.DISPLAYSURF.blit(self.background, (self.x_pos + self.bg_width,0))
    """
    Update the x position of the object and reset it to 0 if it goes beyond the width of the background.
    """
    self.x_pos -= 1
  
    if self.x_pos < -self.bg_width:
        self.x_pos = 0  
