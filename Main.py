import Jirehl
import Patrick
import Jack
import Yazen
import pygame
import Model_Pygame
import Hitboxes

# States
MAIN_MENU = "main_menu"
SELECT_CAMERA = "select_camera"
CALIBRATION = "calibration"
SELECT_DIFFICULTY = "select_difficulty"
SELECT_SKINS = "skins"
SETTINGS = "settings"
SELECT_FRAME_RATE = "select_frame_rate"
GAME_PLAY = "game_play"
GAME_OVER = "game_over"
PAUSE_MENU = "pause_menu"
current_state = MAIN_MENU


# Other declarations
selected_camera_index = -1
selected_difficulty_index = -1
selected_settings_option_index = -1
frame_rate_index = 1

# Main class

if __name__ == "__main__":
    app = Jirehl.Application()
    camera_obj = Patrick.Camera()
    # hitboxes = Jack.Movement()

    screen = app.get_screen()

    skins = Yazen.Skins(screen)

    # model = Model_Pygame.Model()

    while True:
        if frame_rate_index < 0:
            frame_rate_index = 1 # default 30 fps


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
                    if app.on_settings_button():
                        current_state = SETTINGS

        if current_state == SELECT_CAMERA:
            app.select_camera(camera_obj, selected_camera_index)
            camera_obj.stop_camera()
            # model.stop()

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
            # model = Model_Pygame.Model(selected_camera_index) # start cam
            camera_obj.start_camera(selected_camera_index)
            app.calibrate(camera_obj, selected_camera_index,frame_rate_index)

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
                        counted_down = False
                        game = Hitboxes.Game_play(selected_difficulty_index, screen)
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
            if not counted_down:
                app.countdown()
                counted_down = True

            app.start_game(camera_obj,frame_rate_index, game, skins)

            # Collision
            if not game.check_if_alive():
                current_state = GAME_OVER

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if app.on_pause_button():
                        current_state = PAUSE_MENU
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        current_state = PAUSE_MENU

        if current_state == GAME_OVER:
            app.display_game_over_menu() # Change (currently instant screen change, maybe do blur and death effect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if app.on_retry_button():
                        current_state = GAME_PLAY
                        counted_down = False
                        game = Hitboxes.Game_play(selected_difficulty_index, screen)
                    if app.on_quit_button():
                        current_state = MAIN_MENU
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        current_state = GAME_PLAY
                        counted_down = False
                        game = Hitboxes.Game_play(selected_difficulty_index, screen)

        if current_state == PAUSE_MENU:
            app.display_pause_menu()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if app.on_resume_button():
                        current_state = GAME_PLAY
                        counted_down = False
                    if app.on_quit_button():
                        current_state = MAIN_MENU
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        current_state = GAME_PLAY
                        counted_down = False

        if current_state == SETTINGS:
            app.display_settings_menu(selected_settings_option_index)
            # print(selected_settings_option_index)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                        if app.on_back_button():
                            current_state = MAIN_MENU
                        if app.on_confirm_button() and selected_settings_option_index > -1:
                            if selected_settings_option_index == 0:
                                current_state = SELECT_FRAME_RATE
                        else:
                            selected_settings_option_index = app.on_settings_option()
        
        if current_state == SELECT_FRAME_RATE:
            app.select_frame_rate(frame_rate_index)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                        if app.on_back_button():
                            current_state = SETTINGS
                        if app.on_confirm_button() and frame_rate_index > -1:
                            current_state = SETTINGS
                            print(frame_rate_index)
                        else:
                            frame_rate_index = app.on_frame_rate_option()
