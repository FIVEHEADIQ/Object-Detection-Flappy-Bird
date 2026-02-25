"""
Flappy Bird Fit Application Class
By: Jirehl Ngo
2024/01/18
"""

import pygame
import pygame.camera
import Camera
import Skins
import Gameplay

clock = pygame.time.Clock()


class Application():
    """A class to create the graphical user interface
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
        self.width = self.screen.get_width()
        self.height = self.screen.get_height()

        self.color = (255,255,255)
        self.color_light = (170,170,170)
        self.color_dark = (100,100,100)

        # Original font
        # self.bigfont = pygame.font.SysFont('Corbel', 50)
        # self.smallfont = pygame.font.SysFont('Corbel', 20)
        self.bigfont = pygame.font.SysFont("PressStart2P", 20)
        self.smallfont = pygame.font.SysFont("PressStart2P", 8)

        self.frame_rates = ["15", "30", "45", "60"]

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


    def display_main_menu(self, camera: Camera.Camera, selected_camera_index: int, skins: Skins.Skins):
        """Displays the main menu

        Args:
            Camera.camera (camera): Camera object
            int (selected_camera_index): List index of the user selected camera from the pygame list
            Skins.Skins (skins): Skins object

        Returns:
            None
        """
        self.mouse = pygame.mouse.get_pos() # (x,y) tuple

        self.screen.fill(self.color)
        skins.display_background()

        self.display_selected_camera_button(camera, selected_camera_index)
        self.display_title()
        self.display_play_button()
        self.display_skins_button()
        self.display_settings_button()

        pygame.display.update()


    def display_title(self):
        """Displays the title text
        
        Args:
            None

        Returns:
            None
        """
        title_width = 400
        title_height = 45
        title_x = self.width/2 - title_width/2
        title_y = self.height/14 + title_height/2
        title_rect = [title_x, title_y, title_width, title_height]
        pygame.draw.rect(self.screen, self.color_light, title_rect)

        title_text = self.bigfont.render("Flappy Bird Fit", True, self.color)
        self.screen.blit(title_text, (title_x, title_y))


    def display_play_button(self):
        """Displays the 'Play' button
        
        Args:
            None

        Returns:
            None
        """
        self.play_button_width = 155
        self.play_button_height = 45
        self.play_button_x = self.width/2 - self.play_button_width/2
        self.play_button_y = self.height/2
        play_button_rect = [self.play_button_x, self.play_button_y, self.play_button_width, self.play_button_height]

        if self.on_play_button():
            pygame.draw.rect(self.screen, self.color_light, play_button_rect)
        else:
            pygame.draw.rect(self.screen, self.color_dark, play_button_rect)
        
        play_button_text = self.bigfont.render('Play' , True , self.color)
        self.screen.blit(play_button_text, (self.play_button_x + self.play_button_width/4, self.play_button_y))


    def on_play_button(self) -> bool:
        """Returns a boolean value if the cursor is on the 'Play' button or not

        Args:
            None

        Returns:
            bool: If mouse coordinates are within the 'Play' button coordinates and dimensions
        """
        return self.play_button_x <= self.mouse[0] <= self.play_button_x + self.play_button_width and self.play_button_y <= self.mouse[1] <= self.play_button_y + self.play_button_height
    

    def display_skins_button(self):
        """Displays the 'Skins' button
        
        Args:
            None

        Returns:
            None
        """
        self.skins_button_width = 155
        self.skins_button_height = 45
        self.skins_button_x = self.width/2 - self.skins_button_width/2
        self.skins_button_y = self.height/2 + 75
        self.skins_button_rect = [self.skins_button_x, self.skins_button_y, self.skins_button_width, self.skins_button_height]

        if self.on_skins_button():
            pygame.draw.rect(self.screen, self.color_light, self.skins_button_rect)
        else:
            pygame.draw.rect(self.screen, self.color_dark, self.skins_button_rect)

        skins_button_text = self.bigfont.render("Skins", True, self.color)
        self.screen.blit(skins_button_text, (self.skins_button_x + self.skins_button_width/6, self.skins_button_y))


    def on_skins_button(self) -> bool:
        """Returns a boolean value if the cursor is on the 'Skins' button or not

        Args:
            None

        Returns:
            bool: If mouse coordinates are within the 'Skins' button coordinates and dimensions or not
        """
        return self.skins_button_x <= self.mouse[0] <= self.skins_button_x + self.skins_button_width and self.skins_button_y <= self.mouse[1] <= self.skins_button_y + self.skins_button_height


    def display_settings_button(self):
        """Displays the 'Settings' button
        
        Args:
            None

        Returns:
            None
        """
        self.settings_button_width = 155
        self.settings_button_height = 45
        self.settings_button_x = self.width/2 - self.settings_button_width/2
        self.settings_button_y = self.height/2 + 150
        self.settings_button_rect = [self.settings_button_x, self.settings_button_y, self.settings_button_width, self.settings_button_height]

        if self.on_settings_button():
            pygame.draw.rect(self.screen, self.color_light, self.settings_button_rect)
        else:
            pygame.draw.rect(self.screen, self.color_dark, self.settings_button_rect)

        settings_button_text = self.bigfont.render("Settings", True, self.color)
        self.screen.blit(settings_button_text, (self.settings_button_x, self.settings_button_y))


    def on_settings_button(self) -> bool:
        """Returns a boolean value if the cursor is on the 'Settings' button or not

        Args:
            None

        Returns:
            bool: If mouse coordinates are within the 'Settings' button coordinates and dimensions or not
        """
        return self.settings_button_x <= self.mouse[0] <= self.settings_button_x + self.settings_button_width and self.settings_button_y <= self.mouse[1] <= self.settings_button_y + self.settings_button_height


    def display_selected_camera_button(self, camera: Camera.Camera, selected_camera_index: int):
        """Displays the user selected camera on a button

        Args:
            Camera.Camera (camera): Camera object
            int (selected_camera_index): List index for chosen camera

        Returns:
            None
        """
        if selected_camera_index > -1:
            selected_camera = camera.get_cameras()[selected_camera_index]
        else:
            selected_camera = None

        self.selected_camera_x = self.width/100
        self.selected_camera_y = self.height/100
        self.selected_camera_width = 300
        self.selected_camera_height = 20
        self.selected_camera_rect = [self.selected_camera_x, self.selected_camera_y, self.selected_camera_width, self.selected_camera_height]

        if self.on_selected_camera_button():
            pygame.draw.rect(self.screen, self.color_light, self.selected_camera_rect)
        else:
            pygame.draw.rect(self.screen, self.color_dark, self.selected_camera_rect)

        selected_camera_text = self.smallfont.render(f"Selected Camera: {selected_camera}" , True, self.color)
        self.screen.blit(selected_camera_text, (self.selected_camera_x, self.selected_camera_y))


    def on_selected_camera_button(self) -> bool:
        """Returns a boolean value if the cursor is on the 'Selected camera' button or not

        Args:
            None

        Returns:
            bool: If mouse coordinates are within the 'Selected camera' button coordinates and dimensions or not
        """
        return self.selected_camera_x <= self.mouse[0] <= self.selected_camera_x + self.selected_camera_width and self.selected_camera_y <= self.mouse[1] <= self.selected_camera_y + self.selected_camera_height


    def select_camera(self, camera: Camera.Camera, highlighted_camera: int):
        """Displays a menu to select availble cameras

        Args:
            Camera.Camera (camera): Camera object
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

        cameras = camera.get_cameras()

        self.option_x = self.width/2 - self.width/4
        self.option_y_list = []
        self.option_width = 360
        self.option_height = 40
        increment = 0

        # Display 'n' number of camera options
        if len(cameras) > 0:
            for camera in cameras:                
                self.option_y = self.height/4 + increment
                increment += 75

                self.option_rect = [self.option_x, self.option_y, self.option_width, self.option_height]
                self.option_y_list.append(self.option_y)

                if self.on_camera_option() == (increment - 75) / 75 or (increment - 75) / 75 == highlighted_camera:
                    pygame.draw.rect(self.screen, self.color_light, self.option_rect)
                else:
                    pygame.draw.rect(self.screen, self.color_dark, self.option_rect)
                
                camera = str(camera) # Before using OpenCV this actually gave the camera names instead of numbers
                option = self.bigfont.render(camera, True, self.color) 
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

        self.display_back_button()
        self.display_confirm_button()

        select_difficulty_text = self.bigfont.render("Select a Difficulty: ", True, self.color_dark)
        self.screen.blit(select_difficulty_text, (self.width/2 - self.width/4, self.height/12))

        difficulties = ["Easy", "Medium", "Hard", "Professional"] # 'n' = list size

        self.difficulty_x = self.width/2 - self.width/4
        self.difficulty_y_list = []
        self.difficulty_width = 360
        self.difficulty_height = 40
        increment = 0

        # Display 'n' number of difficulties
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
                return i
        return -1


    def display_back_button(self):
        """Displays the 'Back' button

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
        """Returns a boolean value if the cursor is on the 'Back' button or not

        Args:
            None
        
        Returns:
            bool: If mouse coordinates are within the 'Back' button coordinates and dimensions
        """
        return self.back_x <= self.mouse[0] <= self.back_x + self.back_width and self.back_y <= self.mouse[1] <= self.back_y + self.back_height


    def display_confirm_button(self):
        """Displays the 'Confirm' button

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
        """Returns a boolean value if the cursor is on the 'Confirm' button or not

        Args:
            None
        
            
        Returns:
            bool: If mouse coordinates are within the 'Confirm' button coordinates and dimensions
        """
        return self.confirm_x <= self.mouse[0] <= self.confirm_x + self.confirm_width and self.confirm_y <= self.mouse[1] <= self.confirm_y + self.confirm_height


    def calibrate(self, camera: Camera.Camera, selected_camera_index: int, frame_rate_index: int):
        """Displays the camera video as a test

        Args:
            Camera.Camera (camera): Camera object
            int (selected_camera_index): List index for selected camera
            int (frame_rate_index): List index of selected frame rate

        Returns:
            None
        """
        self.mouse = pygame.mouse.get_pos() # (x,y) tuple

        self.screen.fill(self.color)

        model = camera.get_model()
        model.recognize(self.screen, self.width, self.height) 

        self.display_selected_camera_button(camera, selected_camera_index)
        self.display_back_button()
        self.display_confirm_button()

        pygame.display.update()

        # Cap the frame rate
        clock.tick(self.get_frame_rate(frame_rate_index))


    def select_skins(self):
        """Displays the 'Skins' menu

        Args:
            None

        Returns:
            None
        """
        self.mouse = pygame.mouse.get_pos() # (x,y) tuple

        self.screen.fill(self.color)
        
        self.display_back_button()

        pygame.display.update()
    

    def display_settings_menu(self, highlighted_settings_option):
        """Displays a menu to change settings

        Args:
            None

        Returns:
            None
        """
        self.mouse = pygame.mouse.get_pos()

        self.screen.fill(self.color)

        self.display_back_button()
        self.display_confirm_button()

        settings_options_text = self.bigfont.render("Settings", True, self.color_dark)
        self.screen.blit(settings_options_text, (self.width/2 - self.width/4, self.height/12))

        settings_options = ["Frame rate", "Background", "Audio"] # Resolution will be a future update

        self.settings_option_x = self.width/2 - self.width/4
        self.settings_option_y_list = []
        self.settings_option_width = 360
        self.settings_option_height = 40
        increment = 0

        for settings_option in settings_options:
            self.settings_option_y = self.height/4 + increment
            increment += 75

            self.settings_option_rect = [self.settings_option_x, self.settings_option_y, self.settings_option_width, self.settings_option_height]
            self.settings_option_y_list.append(self.settings_option_y)

            if self.on_settings_option() == (increment - 75) / 75 or (increment - 75) / 75 == highlighted_settings_option:
                pygame.draw.rect(self.screen, self.color_light, self.settings_option_rect)
            else:
                pygame.draw.rect(self.screen, self.color_dark, self.settings_option_rect)
            
            settings_option = self.bigfont.render(settings_option, True, self.color)
            self.screen.blit(settings_option, (self.settings_option_x, self.settings_option_y))

        pygame.display.update()


    def on_settings_option(self) -> int:
        """Returns a list index of the settings option the mouse is on
        
        Args:
            None

        Returns:
            int: List index of the settings option the mouse is on
        """
        for i in range(0, len(self.settings_option_y_list)):
            if self.settings_option_x <= self.mouse[0] <= self.settings_option_x + self.settings_option_width and self.settings_option_y_list[i] <= self.mouse[1] <= self.settings_option_y_list[i] + self.settings_option_height:
                return i
        return -1


    def select_frame_rate(self, highlighted_frame_rate_option: int):
        """Displays a screen to select a frame rate
        
        Args:
            int (highlighted_frame_rate_option): List index of currently selected frame rate option

        Returns:
            None
        """
        self.mouse = pygame.mouse.get_pos()

        self.screen.fill(self.color)

        self.display_back_button()
        self.display_confirm_button()

        frame_rate_text = self.bigfont.render("Select a Frame Rate: ", True, self.color_dark)
        self.screen.blit(frame_rate_text, (self.width/2 - self.width/4, self.height/12))

        self.frame_rate_option_x = self.width/2 - self.width/4
        self.frame_rate_option_y_list = []
        self.frame_rate_option_width = 360
        self.frame_rate_option_height = 40
        increment = 0

        for frame_rate in self.frame_rates:
            self.frame_rate_option_y = self.height/4 + increment
            increment += 75

            self.frame_rate_option_rect = [self.frame_rate_option_x, self.frame_rate_option_y, self.frame_rate_option_width, self.frame_rate_option_height]
            self.frame_rate_option_y_list.append(self.frame_rate_option_y)

            if self.on_frame_rate_option() == (increment - 75) / 75 or (increment - 75) / 75 == highlighted_frame_rate_option:
                pygame.draw.rect(self.screen, self.color_light, self.frame_rate_option_rect)
            else:
                pygame.draw.rect(self.screen, self.color_dark, self.frame_rate_option_rect)
            
            frame_rate = self.bigfont.render(frame_rate, True, self.color)
            self.screen.blit(frame_rate, (self.frame_rate_option_x, self.frame_rate_option_y))

        pygame.display.update()



    def on_frame_rate_option(self) -> int:
        """Returns a list index of the frame rate option the mouse is on
        
        Args:
            None

        Returns:
            int: List index of the frame rate option the mouse is on
        """
        for i in range(0, len(self.frame_rate_option_y_list)):
            if self.frame_rate_option_x <= self.mouse[0] <= self.frame_rate_option_x + self.frame_rate_option_width and self.frame_rate_option_y_list[i] <= self.mouse[1] <= self.frame_rate_option_y_list[i] + self.frame_rate_option_height:
                return i
        return -1
    

    def get_frame_rate(self, index) -> int:
        """Returns selected frame rate 
        
        Args:
            None

        Returns:
            int: Selected frame rate
        """
        return int(self.frame_rates[index])
    

    def start_game(self, camera: Camera.Camera, frame_rate_index: int, game: Gameplay.Game_play, skins: Skins.Skins):
        """Start the game

        Args:
            Camera.Camera (camera): Camera object
            int (frame_rate_index): List index of selected frame rate
            Jack.Game_play (game): Game object
            Skins.Skins (skins): Skins object

        Returns:
            None
        """
        self.mouse = pygame.mouse.get_pos() # (x,y) tuple

        model = camera.get_model()
        model.recognize(self.screen, self.width, self.height)

        skins.display_background()

        game.bird_hitbox(model)
        game.bird_skin(skins.get_bird_list()[4])
        game.pipe_hitboxes()

        score = self.bigfont.render(str(game.get_score()), True, self.color)
        self.screen.blit(score, (self.width/2, self.height/20))

        self.display_pause_button()

        pygame.display.update()

        clock.tick(self.get_frame_rate(frame_rate_index))


    def display_pause_button(self):
        """Displays the 'Pause' button

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
        
        self.pause_icon = self.bigfont.render("||", True, self.color)
        self.screen.blit(self.pause_icon, (self.pause_center[0] - 20, self.pause_center[1] - 20))
    

    def on_pause_button(self) -> bool:
        """Returns a boolean value if the cursor is on the 'Pause' button or not

        Args:
            None

        Returns:
            bool: If mouse coordinates are within the 'Pause' button coordinates and dimensions
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

        self.image = self.blur_surface(self.screen, 25)
        self.screen.blit(self.image, (0, 0))

        self.display_resume_button()
        self.display_quit_button()

        pygame.display.update()

        clock.tick(60)


    def display_resume_button(self):
        """Displays the 'Resume' button

        Args:  
            None

        Returns:
            None
        """
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


    def on_resume_button(self) -> bool:
        """Returns a boolean value if the cursor is on the 'Resume' button or not

        Args:
            None

        Returns:
            bool: If mouse coordinates are within the 'Resume' button coordinates and dimensions or not
        """
        return self.resume_x <= self.mouse[0] <= self.resume_x + self.resume_width and self.resume_y <= self.mouse[1] <= self.resume_y + self.resume_height


    def display_quit_button(self):
        """Displays the 'Quit' button

        Args:
            None

        Returns:
            None
        """
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


    def on_quit_button(self) -> bool:
        """Returns a boolean value if the cursor is on the 'Quit' button or not

        Args:
            None

        Returns:
            bool: If mouse coordinates are within the 'Quit' button coordinates and dimensions or not
        """
        return self.quit_x <= self.mouse[0] <= self.quit_x + self.quit_width and self.quit_y <= self.mouse[1] <= self.quit_y + self.quit_height


    def countdown(self):
        """Displays a countdown before starting or resuming the game

        Args:
            None

        Returns:
            None
        """
        start_time = pygame.time.get_ticks()
        delay_duration = 1000
        i = 3
        while i >= 0:
            self.image = self.blur_surface(self.screen, 25)
            self.screen.blit(self.image, (0, 0))

            # Calculate elapsed time
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - start_time

            # Check if the desired delay has passed
            if elapsed_time >= delay_duration:
                i -= 1
                # Reset start time for the next delay
                start_time = pygame.time.get_ticks()

            number = self.bigfont.render(str(i), True, self.color)
            start = self.bigfont.render("Go!", True, self.color)

            if i == 0:
                self.screen.blit(start, (self.width/2, self.height/2))
            elif i > 0:
                self.screen.blit(number, (self.width/2, self.height/2))

            pygame.display.update()


    def blur_surface(self, surface: pygame.surface.Surface, amount: int): # Copy pasted from the internet
        """Blur the given surface by the given 'amount'.  Only values 1 and greater are valid.  Value 1 = no blur.

        Args:
            pygame.surface.Surface (surface): Surface to blur
            int (amount): Blur amount

        Returns:
            pygame.surface.Surface: Blurred surface
        """
        if amount < 1.0:
            raise ValueError("Arg 'amount' must be greater than 1.0, passed in value is %s"%amount)
        scale = 1.0/float(amount)
        surface_size = surface.get_size()
        scale_size = (int(surface_size[0]*scale), int(surface_size[1]*scale))
        surface = pygame.transform.smoothscale(surface, scale_size)
        surface = pygame.transform.smoothscale(surface, surface_size)
        return surface


    def display_game_over_menu(self):
        """Displays the main menu

        Args:
            None

        Returns:
            None
        """
        self.mouse = pygame.mouse.get_pos() # (x,y) tuple

        self.screen.fill(self.color)

        self.display_game_over_text()
        self.display_retry_button()
        self.display_quit_button()

        pygame.display.update()


    def display_game_over_text(self):
        """Displays 'Game Over' text
        
        Args:
            None

        Returns:
            None
        """
        game_over_width = 400
        game_over_height = 45
        game_over_x = self.width/2 - game_over_width/2
        game_over_y = self.height/14 + game_over_height/2
        game_over_rect = [game_over_x, game_over_y, game_over_width, game_over_height]

        pygame.draw.rect(self.screen, self.color_light, game_over_rect)

        game_over_text = self.bigfont.render("Game over", True, self.color)
        self.screen.blit(game_over_text, (game_over_x, game_over_y))

    
    def display_retry_button(self):
        """Displays the 'Retry' button

        Args:
            None

        Returns:
            None
        """
        self.retry_width = 160
        self.retry_height = 45
        self.retry_x = self.width/2 - self.retry_width/2
        self.retry_y = self.height/2 - 70
        self.retry_rect = [self.retry_x, self.retry_y, self.retry_width, self.retry_height]

        if self.on_retry_button():
            pygame.draw.rect(self.screen, self.color_light, self.retry_rect)
        else:
            pygame.draw.rect(self.screen, self.color_dark, self.retry_rect)
        
        retry_text = self.bigfont.render("Retry", True, self.color)
        self.screen.blit(retry_text, (self.retry_x, self.retry_y))

    
    def on_retry_button(self) -> bool:
        """Returns a boolean value of the mouse is on the 'Retry' button or not

        Args:
            None

        Returns:
            bool: If the mouse is on the 'Retry' button or not
        """
        return self.retry_x <= self.mouse[0] <= self.retry_x + self.retry_width and self.retry_y <= self.mouse[1] <= self.retry_y + self.retry_height


    def get_screen(self) -> pygame.surface.Surface:
        """Returns the screen/surface

        Args:
            None
        
        Returns:
            pygame.surface.Surface: screen/surface
        """
        return self.screen
