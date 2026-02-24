import unittest
from unittest.mock import patch
from io import StringIO
from Patrick import Camera, Music  # Assuming your original file is named Patrick.py
import pygame

class TestCamera(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.camera = Camera()

    def tearDown(self):
        pygame.quit()

    def test_get_cameras(self):
        cameras = self.camera.get_cameras()
        self.assertIsInstance(cameras, list)

    @patch('Model_Pygame.Model')
    def test_start_camera(self, mock_model):
        selected_camera_index = 0
        self.camera.start_camera(selected_camera_index)
        self.assertTrue(self.camera.cam_started)
        self.assertIsInstance(self.camera.model, mock_model)

    def test_get_model(self):
        self.assertIsNone(self.camera.get_model())

    def test_stop_camera(self):
        self.camera.cam_started = True
        self.camera.stop_camera()
        self.assertFalse(self.camera.cam_started)

    @patch('pygame.camera.list_cameras')
    def test_refresh_camera_list(self, mock_list_cameras):
        mock_list_cameras.return_value = ['camera1', 'camera2']
        self.camera.refresh_camera_list()
        self.assertEqual(self.camera.cameras, ['camera1', 'camera2'])

class TestMusic(unittest.TestCase):
    def setUp(self):
        pygame.init()
        self.music = Music()

    def tearDown(self):
        pygame.quit()

    def test_play(self):
        with patch('pygame.mixer.music.load') as mock_load, \
             patch('pygame.mixer.music.play') as mock_play:
            self.music.play(0)
            mock_load.assert_called_once_with(self.music.playlist[0])
            mock_play.assert_called_once_with(-1)
            self.assertTrue(self.music.music_played)

    @patch('pygame.mixer.music.unload')
    @patch('pygame.mixer.music.stop')
    def test_stop(self, mock_unload, mock_stop):
        self.music.music_played = True
        self.music.stop()
        mock_unload.assert_called_once()
        mock_stop.assert_called_once()
        self.assertFalse(self.music.music_played)

    def test_set_volume(self):
        with patch('pygame.mixer.music.set_volume') as mock_set_volume:
            self.music.set_volume(0.8)
            mock_set_volume.assert_called_once_with(0.8)

    def test_get_volume(self):
        with patch('pygame.mixer.music.get_volume') as mock_get_volume:
            mock_get_volume.return_value = 0.6
            volume = self.music.get_volume()
            mock_get_volume.assert_called_once()
            self.assertEqual(volume, 0.6)

if __name__ == '__main__':
    unittest.main()
