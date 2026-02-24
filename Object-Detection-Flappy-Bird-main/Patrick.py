"""
Flappy Bird Fit
By: Patrick Liu
https://www.programiz.com/python-programming/docstrings
"""

import pygame
import pygame.camera

class Camera():
    """Class which initializes camera in Pygame GUI

    Attributes
    ----------
    None

    Methods
    -------
    __init__():
        Constructor for Camera Object

    get_cameras():
        Gettor method users Cameras

    start_camera(selected_camera_index):
        Starts camera using user selected Camera

    get_model():
        Getter method for yolov8 model from Model_pygame.py
 
    stop_camera():
        Stops Camera

    refresh_camera_list():
        Loads list of available cameras user has
    """
    def __init__(self):
        """Initalizes Camera object
        """
        pygame.camera.init()
        self.refresh_camera_list()
        self.cam_started = False

    def get_cameras(self):
        """Gettor method for all cameras user has

        Returns:
            List[str]: Cameras user has
        """
        return self.cameras

    def start_camera(self, selected_camera_index):
        import Model_Pygame
        """Starts camera based on selected camera from user

        Parameters:
                selected_camera_index (int): Selected camera of user

        """
        if not self.cam_started:
            self.model = Model_Pygame.Model(selected_camera_index)
            self.cam_started = True

    def get_model(self):
        return self.model

    def stop_camera(self):
        """
        """
        if self.cam_started:
            self.cam_started = False
            self.model.stop()

    def refresh_camera_list(self):
        """Loads a list of all available cameras
        """
        self.cameras = pygame.camera.list_cameras()

class Music: 
    """Class for playing music while the user is in the menu, or any of the game difficulties
    
    Attributes
    ----------
    playlist : list[str]
        List of files for each song
    music_played : bool
        Boolean value which represents if music is currently playing
    music_stopped : bool
        Boolean value which represents if music is currently stopped
        
    Methods
    -------
    __init__():
        Constructor which initializes the music object

    play(index, loop=-1):
        Start playing music, repeats if music is ended

    stop():
        Stops music

    set_volume(volume):
        Change volume of music, 0.0 for minimum, 1.0 for maximum

    get_volume():
        Getter method for current volume
    """

    def __init__(self):
        """Constructor for Music Object
        """
        import os
        pygame.mixer.init()
        # Get absolute paths for each music file
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.playlist = [
            os.path.join(script_dir, "22-01. Super Smash Bros. Brawl Main Theme.mp3"),
            os.path.join(script_dir, "01 Title Theme.mp3"),
            os.path.join(script_dir, "1-17. Accumula Town.mp3"),
            os.path.join(script_dir, "4-12. Battle! (Champion).mp3"),
            os.path.join(script_dir, "645631_Lunar-Abyss.mp3")
        ]
        self.music_played = False
        self.music_stopped = False

    def play(self, index, loop=-1):
        """
        Starts music

        Parameters:
        index (int): Indice of current song in the playlist
        loop (int): Number of times to loop the music, currently looping infinitely.
        """
        if not self.music_played:
            pygame.mixer.music.load(self.playlist[index])
            pygame.mixer.music.play(loop)
            self.music_played = True

    def stop(self):
        """Stops music
        """
        if not self.music_stopped:
            pygame.mixer.music.unload()
            pygame.mixer.music.stop()
            self.music_played = False

    def set_volume(self, volume):
        """
        Setter method for volume of music

        Parameters:
        volume (float): Volume level (0.0 to 1.0)
        """
        pygame.mixer.music.set_volume(volume)

    def get_volume(self):
        """
        Getter method for volume of music

        Returns:
        float: The current volume level (0.0 to 1.0)
        """
        return pygame.mixer.music.get_volume()
