import unittest
from unittest.mock import MagicMock, patch
from Jirehl import Application 

class TestMainMenuDisplay(unittest.TestCase):

    def setUp(self):
        self.application_instance = Application()

    def test_display_main_menu(self):
        # Mocking required dependencies
        camera_mock = MagicMock()
        skins_mock = MagicMock()
        pygame_mock = MagicMock()

        with patch('Jirehl.pygame', pygame_mock):
            # Mocking pygame.mouse.get_pos() method
            pygame_mock.mouse.get_pos.return_value = (10, 20)

            # Mocking pygame.display.update() method
            with patch('Jirehl.pygame.display.update') as display_update_mock:
                # Calling the method to be tested
                self.application_instance.display_main_menu(camera_mock, 0, skins_mock)

                # Asserting that the necessary methods were called
                pygame_mock.mouse.get_pos.assert_called_once()
                self.assertTrue(display_update_mock.called)

    # Add more test cases if needed

if __name__ == '__main__':
    unittest.main()
