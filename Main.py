import pygame
import sys
import pygame.camera
from pygame.constants import MOUSEBUTTONDOWN
from pygame.display import set_allow_screensaver
import pygame.locals
import Model_Pygame
import os

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

# Main class
app = Application()
camera_obj = Camera()
patrick = Model_Pygame.Patrick()

while True:
    if current_state == MAIN_MENU:
        app.display_main_menu(camera_obj, selected_camera_index)

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if app.on_play_button():
                    if selected_camera_index > -1:
                        current_state = SELECT_DIFFICULTY
                    else:
                        current_state = SELECT_CAMERA
                if app.on_skins_button():
                    current_state = SELECT_SKINS
                if app.on_selected_camera_button():
                    current_state = SELECT_CAMERA

    if current_state == SELECT_CAMERA:
        app.select_camera(camera_obj, selected_camera_index)
        camera_obj.stop_camera()

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if app.on_back_button():
                    current_state = MAIN_MENU

                if app.on_confirm_button() and selected_camera_index > -1:
                    app.display_loading_screen()
                    current_state = CALIBRATION
                else: 
                    selected_camera_index = app.on_camera_option()
                
    if current_state == CALIBRATION:
        app.calibrate(camera_obj, selected_camera_index, patrick)

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if app.on_back_button():
                    current_state = SELECT_CAMERA
                if app.on_confirm_button():
                    current_state = MAIN_MENU

    if current_state == SELECT_DIFFICULTY:
        app.select_difficulty(selected_difficulty_index)

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if app.on_back_button():
                    current_state = MAIN_MENU
                if app.on_confirm_button() and selected_difficulty_index > -1:
                    current_state = GAME_PLAY
                else:
                    selected_difficulty_index = app.on_difficulty()

    if current_state == SELECT_SKINS:
        app.select_skins()

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if app.on_back_button():
                    current_state = MAIN_MENU
    
    if current_state == GAME_PLAY:
        app.start_game(camera_obj, selected_camera_index, selected_difficulty_index, patrick)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if app.on_pause_button():
                    current_state = PAUSE_MENU
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_state = PAUSE_MENU

    if current_state == PAUSE_MENU:
        app.display_pause_menu()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if app.on_resume_button():
                    current_state = GAME_PLAY
                if app.on_quit_button():
                    current_state = MAIN_MENU
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    current_state = GAME_PLAY