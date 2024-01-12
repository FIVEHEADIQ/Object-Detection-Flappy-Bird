"""
Pushup Flappy Bird
By: Jirehl Ngo
https://www.programiz.com/python-programming/docstrings
"""

import pygame
import sys
import pygame.camera
from pygame.constants import MOUSEBUTTONDOWN
from pygame.display import set_allow_screensaver
import pygame.locals
import os
import Patrick
import Model_Pygame

# States
MAIN_MENU = "main_menu"
SELECT_CAMERA = "select_camera"
CALIBRATION = "calibration"
SELECT_DIFFICULTY = "select_difficulty"
SELECT_SKINS = "skins"
SETTINGS = "settings"
GAME_PLAY = "game_play"
PAUSE_MENU = "pause_menu"
current_state = MAIN_MENU

# Other declarations
clock = pygame.time.Clock()
cam_started = False
selected_camera_index = -1
selected_difficulty_index = -1

class Application():
    """A class to create the application interface
    """
    def __init__(self):
        """Constructor for Application Class, sets up the Pygame screen/surface

        Args:
            None

        Returns:
            None
        """
        pygame.init()
        resolution = (720,480)
        self.screen = pygame.display.set_mode(resolution)
        # print(type(self.screen))
        self.color = (255,255,255)  
        self.color_light = (170,170,170)  
        self.color_dark = (100,100,100)  
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        # self.bigfont = pygame.font.SysFont('Corbel', 50) # OG corbel, 50
        # self.smallfont = pygame.font.SysFont('Corbel', 20)  # OG corbel, 20
        self.bigfont = pygame.font.SysFont('PressStart2P', 20) # OG corbel, 50
        self.smallfont = pygame.font.SysFont('PressStart2P', 8)  # OG corbel, 20

        self.display_loading_screen()


    def display_loading_screen(self):
        """Displays a loading screen for when there will be short wait times

        Args:
            None
        
        Returns:
            None
        """
        self.screen.fill(self.color)
        loading_text = self.bigfont.render("Loading...", True, self.color_dark)
        self.screen.blit(loading_text, (0, self.height - 60))
        pygame.display.update()


    def display_main_menu(self, camera: Patrick.Camera, selected_camera_index: int):
        """Displays the main menu

        Args:
            Camera (camera): camera object
            int (selected_camera_index): List index of the user selected camera from the pygame list

        Returns:
            None
        """
        self.mouse = pygame.mouse.get_pos() # (x,y) tuple
        self.screen.fill(self.color)
        self.display_selected_camera(camera, selected_camera_index)

        # Title
        title_text = self.bigfont.render("Pushup Flappy Bird", True, self.color)

        title_width = 400
        title_height = 45
        title_x = self.width/2 - title_width/2
        title_y = self.height/14 + title_height/2

        title_rect = [title_x, title_y, title_width, title_height]

        pygame.draw.rect(self.screen, self.color_light, title_rect)
        self.screen.blit(title_text, (title_x, title_y))


        # Play button
        play_button_text = self.bigfont.render('Play' , True , self.color)

        self.play_button_width = 140
        self.play_button_height = 45
        self.play_button_x = self.width/2 - self.play_button_width/2
        self.play_button_y = self.height/2

        play_button_rect = [self.play_button_x, self.play_button_y, self.play_button_width, self.play_button_height]

        if self.on_play_button():
            pygame.draw.rect(self.screen, self.color_light, play_button_rect)
        else:
            pygame.draw.rect(self.screen, self.color_dark, play_button_rect)
        
        self.screen.blit(play_button_text, (self.play_button_x + self.play_button_width/5, self.play_button_y))
        

        # Skins button
        self.skins_button_width = 140
        self.skins_button_height = 45
        self.skins_button_x = self.width/2 - self.skins_button_width/2
        self.skins_button_y = self.height/2 + 75

        self.skins_button_rect = [self.skins_button_x, self.skins_button_y, self.skins_button_width, self.skins_button_height]

        if self.on_skins_button():
            pygame.draw.rect(self.screen, self.color_light, self.skins_button_rect)
        else:
            pygame.draw.rect(self.screen, self.color_dark, self.skins_button_rect)

        skins_button_text = self.bigfont.render("Skins", True, self.color)
        self.screen.blit(skins_button_text, (self.skins_button_x + self.skins_button_width/8, self.skins_button_y))


        # Settings button

        pygame.display.update()

      # destination_surface.blit(source_surface, dest_position, area=None, special_flags=0)


    def on_play_button(self) -> bool:
        """Returns a boolean value if the cursor is on the 'play' button or not

        Args:
            None

        Returns:
            bool: If mouse coordinates are within the 'play' button coordinates and dimensions
        """
        return self.play_button_x <= self.mouse[0] <= self.play_button_x + self.play_button_width and self.play_button_y <= self.mouse[1] <= self.play_button_y + self.play_button_height
    

    def on_skins_button(self) -> bool:
        """Returns a boolean value if the cursor is on the 'skins' button or not

        Args:
            None

        Returns:
            bool: If mouse coordinates are within the 'skins' button coordinates and dimensions
        """
        return self.skins_button_x <= self.mouse[0] <= self.skins_button_x + self.skins_button_width and self.skins_button_y <= self.mouse[1] <= self.skins_button_y + self.skins_button_height

    def on_settings_button(self) -> bool:
        """Returns a boolean value if the cursor is on the 'settings' button or not

        Args:
            None

        Returns:
            bool: If mouse coordinates are within the 'settings' button coordinates and dimensions
        """
        pass


    def display_selected_camera(self, camera: Patrick.Camera, selected_camera_index: int):
        """Displays the user selected camera

        Args:
            Camera (camera): Camera object
            int (selected_camera_index): List index for chosen camera

        Returns:
            None
        """
        selected_camera = None
        if selected_camera_index > -1:
            selected_camera = camera.get_cameras()[selected_camera_index]
        self.selected_camera_x = self.width/100
        self.selected_camera_y = self.height/100
        self.selected_camera_width = 300
        self.selected_camera_height = 20
        self.selected_camera_rect = [self.selected_camera_x, self.selected_camera_y, self.selected_camera_width, self.selected_camera_height]

        selected_camera_text = self.smallfont.render(f"Selected Camera: {selected_camera}" , True, self.color)
        if self.on_selected_camera_button():
            pygame.draw.rect(self.screen, self.color_light, self.selected_camera_rect)
        else:
            pygame.draw.rect(self.screen, self.color_dark, self.selected_camera_rect)
        self.screen.blit(selected_camera_text, (self.selected_camera_x, self.selected_camera_y))


    def on_selected_camera_button(self) -> bool:
        """Returns a boolean value if the cursor is on the 'selected camera' button or not

        Args:
            None

        Returns:
            bool: If mouse coordinates are within the 'selected camera' button coordinates and dimensions
        """
        return self.selected_camera_x <= self.mouse[0] <= self.selected_camera_x + self.selected_camera_width and self.selected_camera_y <= self.mouse[1] <= self.selected_camera_y + self.selected_camera_height


    def select_camera(self, camera: Patrick.Camera, highlighted_camera: int):
        """Displays a menu to select availble cameras

        Args:
            Camera (camera): Camera object
            int (highlighted_camera): List index of camera currently selected (not confirmed)
        
        Returns:
            None
            
        """
        self.mouse = pygame.mouse.get_pos() # (x,y) tuple
        self.screen.fill(self.color)
        self.display_back_button()
        self.display_confirm_button()

        available = self.bigfont.render("Available Cameras: ", True, self.color_dark)
        self.screen.blit(available, (self.width/2 - self.width/4, self.height/12))

        cameras = camera.get_cameras() # HEREERERERERERERERERERERERERE
        # cameras.append("Test")
        # cameras.append("Test2")
        # cameras.pop(0)
        increment = 0
        # cameras can just be cameras as of Jan 9th
        self.option_x = self.width/2 - self.width/4
        self.option_y_list = []
        self.option_width = 360
        self.option_height = 40

        # ERROR CATCH: if no cameras (with refresh button)
        if len(cameras) > 0:
            for camera in cameras:
                camera = str(camera)
                self.option_y = self.height/4 + increment
                increment += 75

                self.option_rect = [self.option_x, self.option_y, self.option_width, self.option_height]
                self.option_y_list.append(self.option_y)

                if self.on_camera_option() == (increment - 75) / 75 or (increment - 75) / 75 == highlighted_camera:
                    pygame.draw.rect(self.screen, self.color_light, self.option_rect)
                else:
                    pygame.draw.rect(self.screen, self.color_dark, self.option_rect)
                
                option = self.bigfont.render(camera, True, self.color) # Change camera to 0?
                self.screen.blit(option, (self.option_x, self.option_y))
        else:
            pygame.draw.rect(self.screen, self.color_dark, [self.option_x, self.height/4, self.option_width, self.option_height])
            no_cameras = self.bigfont.render("None found", True, self.color)
            self.screen.blit(no_cameras, (self.option_x, self.height/4))

        pygame.display.update()


    def on_camera_option(self) -> int:
        """Returns the index of the camera option the cursor is on

        Args:
            None

        Returns:
            int: List index of the camera option where the mouse coordinates are within its button coordinates and dimensions
        """
        for i in range(0, len(self.option_y_list)):
            if self.option_x <= self.mouse[0] <= self.option_x + self.option_width and self.option_y_list[i] <= self.mouse[1] <= self.option_y_list[i] + self.option_height:
                return i
        return -1

    
    def select_difficulty(self, highlighted_difficulty: int):
        """Displays a menu to select a difficulty

        Args:
            int (highlighted_difficulty): Diffculty currently selected (not confirmed)

        Returns:
            None
        """
        self.mouse = pygame.mouse.get_pos() # (x,y) tuple
        self.screen.fill(self.color)
        difficulties = ["Easy", "Medium", "Hard", "Professional"] # Maybe display high scores
        self.display_back_button()
        self.display_confirm_button()

        select_difficulty_text = self.bigfont.render("Select a Difficulty: ", True, self.color_dark)
        self.screen.blit(select_difficulty_text, (self.width/2 - self.width/4, self.height/12))

        increment = 0

        self.difficulty_x = self.width/2 - self.width/4
        self.difficulty_y_list = []
        self.difficulty_width = 360
        self.difficulty_height = 40

        for difficulty in difficulties:
            self.difficulty_y = self.height/4 + increment
            increment += 75
            self.difficulty_rect = [self.difficulty_x, self.difficulty_y, self.difficulty_width, self.difficulty_height]

            self.difficulty_y_list.append(self.difficulty_y)

            if self.on_difficulty() == (increment - 75) / 75 or (increment - 75) / 75 == highlighted_difficulty:
                pygame.draw.rect(self.screen, self.color_light, self.difficulty_rect)
            else:
                pygame.draw.rect(self.screen, self.color_dark, self.difficulty_rect)
            
            difficulty = self.bigfont.render(difficulty, True, self.color)
            self.screen.blit(difficulty, (self.difficulty_x, self.difficulty_y))

        pygame.display.update()


    def on_difficulty(self) -> int:
        """Returns the index of the difficulty the cursor is on

        Args:
            None
        
        Returns:
            int: List index of the difficulty option where the mouse coordinates are within its button coordinates and dimensions
        """
        for i in range(0, len(self.difficulty_y_list)):
            if self.difficulty_x <= self.mouse[0] <= self.difficulty_x + self.difficulty_width and self.difficulty_y_list[i] <= self.mouse[1] <= self.difficulty_y_list[i] + self.difficulty_height:
                # pass # Return numbers
                return i
        return -1


    def display_back_button(self):
        """Displays the 'back' button

        Args:
            None
        
        Returns:
            None
        """
        self.back_x = self.width/40
        self.back_y = self.height - self.height/8
        self.back_width = 165
        self.back_height = 40
        self.back_rect = [self.back_x, self.back_y, self.back_width, self.back_height]

        if self.on_back_button():
            pygame.draw.rect(self.screen, self.color_light, self.back_rect)
        else:
            pygame.draw.rect(self.screen, self.color_dark, self.back_rect)
        back_text = self.bigfont.render("Back", True, self.color)
        self.screen.blit(back_text, (self.back_x, self.back_y))
        

    def on_back_button(self) -> bool:
        """Returns a boolean value if the cursor is on the 'back' button or not

        Args:
            None
        
        Returns:
            bool: If mouse coordinates are within the 'back' button coordinates and dimensions
        """
        return self.back_x <= self.mouse[0] <= self.back_x + self.back_width and self.back_y <= self.mouse[1] <= self.back_y + self.back_height


    def display_confirm_button(self):
        """Displays the 'confirm' button

        Args:
            None

        Returns:
            None
        """
        self.confirm_x = self.width - self.width/4
        self.confirm_y = self.height - self.height/8
        self.confirm_width = 165
        self.confirm_height = 40
        self.confirm_rect = [self.confirm_x, self.confirm_y, self.confirm_width, self.confirm_height]

        if self.on_confirm_button():
            pygame.draw.rect(self.screen, self.color_light, self.confirm_rect)
        else:
            pygame.draw.rect(self.screen, self.color_dark, self.confirm_rect)
        confirm_text = self.bigfont.render("Confirm", True, self.color)
        self.screen.blit(confirm_text, (self.confirm_x, self.confirm_y))


    def on_confirm_button(self) -> bool:
        """Returns a boolean value if the cursor is on the 'confirm' button or not

        Args:
            None
        
            
        Returns:
            bool: If mouse coordinates are within the 'confirm' button coordinates and dimensions
        """
        return self.confirm_x <= self.mouse[0] <= self.confirm_x + self.confirm_width and self.confirm_y <= self.mouse[1] <= self.confirm_y + self.confirm_height


    def calibrate(self, camera: Patrick.Camera, selected_camera_index: int, model: Model_Pygame.Model):
        """Displays the camera video as a test

        Args:
            Camera (camera): Camera object
            int (selected_camera_index): List index for selected camera

        Returns:
            None
        """
        self.mouse = pygame.mouse.get_pos() # (x,y) tuple
        camera.start_camera(selected_camera_index)
        # image = camera.get_image()

        # Resize the captured frame to fit the screen
        # image = pygame.transform.scale(image, (self.width, self.height))

        # Fill the entire window with the background color
        self.screen.fill(self.color)

        # Draw the captured frame onto the screen
        # self.screen.blit(image, (0, 0))
        model.recognize(self.screen, self.width, self.height)
        self.display_selected_camera(camera, selected_camera_index)
        self.display_back_button()
        self.display_confirm_button()

        # Update the display
        pygame.display.update()

        # Cap the frame rate
        clock.tick(60)


    def select_skins(self):
        """Displays the skins menu

        Args:
            None

        Returns:
            None
        """
        self.mouse = pygame.mouse.get_pos() # (x,y) tuple
        self.screen.fill(self.color)
        
        self.display_back_button()

        pygame.display.update()
    

    def settings(self):
        """Displays a menu to change settings

        Args:
            None

        Returns:
            None
        """
        pass # Change frame rate, sound, hide background


    def start_game(self, camera: Patrick.Camera, selected_camera_index, selected_difficulty_index, model: Model_Pygame.Model):
        """Start the game

        Args:
            Camera (camera): Camera object

        Returns:
            None
        """
        self.mouse = pygame.mouse.get_pos() # (x,y) tuple
        # self.image = camera.get_image()

        # Resize the captured frame to fit the screen
        # self.image = pygame.transform.scale(self.image, (self.width, self.height))

        # Fill the entire window with the background color
        self.screen.fill(self.color)

        # Draw the captured frame onto the screen
        # self.screen.blit(self.image, (0, 0))
        model.recognize(self.screen, self.width, self.height)
        self.display_pause_button()

        # Update the display
        pygame.display.update()

        # Cap the frame rate
        clock.tick(60)


    def display_pause_button(self):
        """Displays the 'pause' button

        Args:
            None

        Returns:
            None
        """
        self.pause_center = (self.width/15, self.height/10)
        self.pause_radius = 40

        if self.on_pause_button():
            pygame.draw.circle(self.screen, self.color_light, self.pause_center, self.pause_radius)
        else:
            pygame.draw.circle(self.screen, self.color_dark, self.pause_center, self.pause_radius)
        
        self.pause_icon = self.bigfont.render("| |", True, self.color)
        self.screen.blit(self.pause_icon, (self.pause_center[0] - 16, self.pause_center[1] - 25))
    

    def on_pause_button(self) -> bool:
        """Returns a boolean value if the cursor is on the 'pause' button or not

        Args:
            None

        Returns:
            bool: If mouse coordinates are within the 'pause' button coordinates and dimensions
        """
        return self.pause_center[0] - self.pause_radius <= self.mouse[0] <= self.pause_center[0] + self.pause_radius and self.pause_center[1] - self.pause_radius <= self.mouse[1] <= self.pause_center[1] + self.pause_radius


    def display_pause_menu(self):
        """Displays a pause menu

        Args:
            None

        Returns:
            None
        """
        self.mouse = pygame.mouse.get_pos() # (x,y) tuple
        # self.image = camera.get_image()
        self.image = self.blur_surface(self.screen, 25)

        # Resize the captured frame to fit the screen
        # self.image = pygame.transform.scale(self.image, (self.width, self.height)) # take last frame

        # Fill the entire window with the background color
        # self.screen.fill(self.color)

        # Draw the captured frame onto the screen
        self.screen.blit(self.image, (0, 0))
        # pygame.transform.smoothscale(self.screen, (1, 1))
        # pygame.transform.smoothscale(self.screen, (720, 480))
        # self.display_selected_camera(camera, selected_camera_index)
        # self.display_back_button()
        # self.display_confirm_button()
        # self.display_pause_button()


        # Resume button
        self.resume_width = 160
        self.resume_height = 45
        self.resume_x = self.width/2 - self.resume_width/2
        self.resume_y = self.height/2 - 70
        self.resume_rect = [self.resume_x, self.resume_y, self.resume_width, self.resume_height]

        if self.on_resume_button():
            pygame.draw.rect(self.screen, self.color_light, self.resume_rect)
        else:
            pygame.draw.rect(self.screen, self.color_dark, self.resume_rect)
        
        resume_text = self.bigfont.render("Resume", True, self.color)
        self.screen.blit(resume_text, (self.resume_x, self.resume_y))


        # Quit button
        self.quit_width = 160
        self.quit_height = 45
        self.quit_x = self.width/2 - self.quit_width/2
        self.quit_y = self.height/2 
        self.quit_rect = [self.quit_x, self.quit_y, self.quit_width, self.quit_height]

        if self.on_quit_button():
            pygame.draw.rect(self.screen, self.color_light, self.quit_rect)
        else:
            pygame.draw.rect(self.screen, self.color_dark, self.quit_rect)

        quit_text = self.bigfont.render("Quit", True, self.color)
        self.screen.blit(quit_text, (self.quit_x, self.quit_y))

        # Update the display
        pygame.display.update()

        # Cap the frame rate
        clock.tick(60)


    def on_resume_button(self) -> bool:
        """Returns a boolean value if the cursor is on the 'resume' button or not

        Args:
            None

        Returns:
            bool: If mouse coordinates are within the 'resume' button coordinates and dimensions
        """
        return self.resume_x <= self.mouse[0] <= self.resume_x + self.resume_width and self.resume_y <= self.mouse[1] <= self.resume_y + self.resume_height


    def on_quit_button(self) -> bool:
        """Returns a boolean value if the cursor is on the 'quit' button or not

        Args:
            None

        Returns:
            bool: If mouse coordinates are within the 'quit' button coordinates and dimensions
        """
        return self.quit_x <= self.mouse[0] <= self.quit_x + self.quit_width and self.quit_y <= self.mouse[1] <= self.quit_y + self.quit_height


    def countdown(self):
        """Displays a countdown before starting or resuming the game

        Args:
            None

        Returns:
            None
        """
        pass # 3, 2, 1...


    def blur_surface(self, surface: pygame.surface.Surface, amt: int): # Copy pasted from the internet
        """Blur the given surface by the given 'amount'.  Only values 1 and greater are valid.  Value 1 = no blur.

        Args:
            pygame.surface.Surface (surface): Surface to blur
            int (amt): Blur value

        Returns:
            pygame.surface.Surface: Blurred surface
        """
        if amt < 1.0:
            raise ValueError("Arg 'amt' must be greater than 1.0, passed in value is %s"%amt)
        scale = 1.0/float(amt)
        surf_size = surface.get_size()
        scale_size = (int(surf_size[0]*scale), int(surf_size[1]*scale))
        surf = pygame.transform.smoothscale(surface, scale_size)
        surf = pygame.transform.smoothscale(surf, surf_size)
        return surf
