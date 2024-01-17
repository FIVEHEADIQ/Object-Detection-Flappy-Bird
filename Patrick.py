"""
Pushup Flappy Bird
By: Patrick Liu
https://www.programiz.com/python-programming/docstrings
"""

import Model_Pygame
import cv2
import pygame
import pygame.camera

cam_started = False

class Camera(): # Make all the methods static, remove need for camera object?
    """A class to initialize a camera
    """
    def __init__(self):
        """Constructor
        """
        pygame.camera.init()
        self.refresh_camera_list()
    def get_cameras(self):
        # self.cameras = pygame.camera.list_cameras() 
        # print(self.cameras) # Testing
        return self.cameras
    def start_camera(self, selected_camera_index):
        global cam_started
        if not cam_started:
            # print(selected_camera_index) # Getting -1 RESOLVED
            self.model = Model_Pygame.Model(selected_camera_index)
            cam_started = True
    def get_model(self):
        return self.model
    def stop_camera(self):
        """
        """
        global cam_started
        if cam_started:
            cam_started = False
            self.model.stop()
    def get_image(self):
        """Returns a frame from the video feed
        """
        image = self.cam.get_image()
        return pygame.transform.flip(image, True, False)
    def refresh_camera_list(self):
        """Loads a list of all available cameras
        """
        self.cameras = pygame.camera.list_cameras()

class Music: 
    """Class for playing arcade style music while the user is in thee game
    """
    
    def __init__(self):
        """
        Constructor which initalizes the class with a given file

        Parameters:
        music_file (str): Path in files to the music file
        """
        pygame.mixer.init()
        self.playlist = []
        self.current_song_index = 0

    def add_song(self, music_file):
        """
        Add a song to the playlist.

        Parameters:
        - music_file (str): The path to the music file.
        """
        self.playlist.append(pygame.mixer.Sound(music_file))

    def play(self, loop=-1):
        """
        Start playing the music.

        Parameters:
        loop (int): Number of times to loop the music. Set to -1 for infinite loop.
        """
        pygame.mixer.music.play(loop)
        
    def next_song(self):
        """Switch to the next song in the playlist."""
        self.stop()
        self.current_song_index = (self.current_song_index + 1) % len(self.playlist)
        self.play()
        
    def pause(self):
        """Pause the currently playing music."""
        pygame.mixer.music.pause()

    def unpause(self):
        """Unpause the currently paused music."""
        pygame.mixer.music.unpause()

    def stop(self):
        """Stop playing the music."""
        pygame.mixer.music.stop()

    def set_volume(self, volume):
        """
        Set the volume level of the music.

        Parameters:
        volume (float): Volume level (0.0 to 1.0).
        """
        pygame.mixer.music.set_volume(volume)

    def get_volume(self):
        """
        Get the current volume level of the music.

        Returns:
        float: The current volume level (0.0 to 1.0).
        """
        return pygame.mixer.music.get_volume()
    
music_player = Music()
music_player.play()
