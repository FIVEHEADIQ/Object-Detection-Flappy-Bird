"""
Module for initializing game window and handling user input for quitting the game.
"""
import os
import pygame
from pygame.locals import QUIT

class Skins:
  """
  Initializes the display surface and sets up the paths for image assets
  DISPLAYSURF: the display surface for rendering everything
  """
  def __init__(self, DISPLAYSURF: pygame.surface.Surface):
    self.DISPLAYSURF = DISPLAYSURF
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # All available backgrounds in the skins subfolder
    self.background_list = [
        'skins/background.jpg',
        'skins/background2.jpg',
        'skins/background3.jpg',
        'skins/background4.jpg',
    ]
    self.background_names = ["Default", "Night", "Desert", "Forest"]

    # Filter to only backgrounds that actually exist on disk
    self.background_list = [
        p for p in self.background_list
        if os.path.exists(os.path.join(script_dir, *p.split('/')))
    ]
    self.background_names = self.background_names[:len(self.background_list)]

    # Fallback: if only one or zero found, ensure at least the default is listed
    if not self.background_list:
        self.background_list = ['skins/background.jpg']
        self.background_names = ["Default"]

    self.selected_bg_index = 0
    self._load_background(script_dir)

    self.bg_width = self.background.get_width()
    self.x_pos = 0

    self.bird_list = [
        'skins/Blue Man.png',
        'skins/Green Hat Man.png',
        'skins/Pink Man.png',
        'skins/Pixel Blue Man.png',
        'skins/Pixel Yellow Man.png',
        'skins/Yellow Hat Man.png',
    ]
    self.selected_bird_index = 0

  def _load_background(self, script_dir=None):
    """Load and scale the currently selected background."""
    if script_dir is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
    bg_path = os.path.join(script_dir, *self.background_list[self.selected_bg_index].split('/'))
    self.background = pygame.image.load(bg_path).convert()
    self.background = pygame.transform.smoothscale(self.background, self.DISPLAYSURF.get_size())
    self.bg_width = self.background.get_width()
    self.x_pos = 0

  def set_background(self, index: int):
    """Switch the active background by index."""
    if 0 <= index < len(self.background_list):
        self.selected_bg_index = index
        self._load_background()

  def get_background_list(self):
    return self.background_list

  def get_background_names(self):
    return self.background_names

  def get_selected_bg_index(self) -> int:
    return self.selected_bg_index

  def set_bird(self, index: int):
    """Switch the active bird skin by index."""
    if 0 <= index < len(self.bird_list):
        self.selected_bird_index = index

  def get_selected_bird_index(self) -> int:
    return self.selected_bird_index

  def get_bird_list(self):
    return self.bird_list

  def display_background(self):
    """
    Display the background image on the display surface in a shifting pattern.
    """
    self.DISPLAYSURF.blit(self.background, (self.x_pos, 0))
    self.DISPLAYSURF.blit(self.background, (self.x_pos + self.bg_width, 0))
    self.x_pos -= 1
    if self.x_pos < -self.bg_width:
        self.x_pos = 0