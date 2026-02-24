import unittest
import pygame
from Yazen import Skins  

class TestSkins(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.DISPLAYSURF = pygame.display.set_mode((800, 600))
        self.skins = Skins(self.DISPLAYSURF)

    def test_display_background(self):
        # Ensure that the display_background method works without errors
        self.skins.display_background()

    def test_update_background_position(self):
        # Ensure that the background position is updated correctly
        initial_x_pos = self.skins.x_pos
        self.skins.display_background()
        self.assertNotEqual(initial_x_pos, self.skins.x_pos)

    def test_get_bird_list(self):
        # Ensure that the get_bird_list method returns a non-empty list
        bird_list = self.skins.get_bird_list()
        self.assertIsInstance(bird_list, list)
        self.assertGreater(len(bird_list), 0)

if __name__ == '__main__':
    unittest.main()