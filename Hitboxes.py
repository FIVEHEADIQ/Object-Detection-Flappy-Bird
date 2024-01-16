import Model_Pygame
import pygame
import random

class Game_play:
    def __init__(self, pipe_nums):
        self.speed = 20
        self.pipe_width = 45
        self.pipe_height = 720
        self.pipe_gap = 100
        self.pipe_nums = pipe_nums
        self.bird_x = 200
        self.game_resetted = False

        self.score = 0

        self.color = (0, 255, 6)
    
    def bird_hitbox(self, screen, model: Model_Pygame.Model):
        self.bird_y = model.get_y_pos() + 120
        pygame.draw.circle(screen, self.color, (self.bird_x, self.bird_y), 15) # Color OG: 0, 0, 6

    def pipe_hitboxes(self, screen):
        for i in range(0, self.pipe_nums):
            if not self.game_resetted:
                pipe_gap_y = random.randint(140, 480 - self.pipe_gap - 20)
                pipe_x = 720 + 180 * self.pipe_nums #figure out a way to run this only once
            if pipe_x < -self.pipe_width: 
                pipe_x = 720 # Change
                pipe_gap_y = random.randint(140, 480 - self.pipe_gap - 20)
                passed_pipe = False

            # Upper pipe
            # pipe_x = screen.get_width()
            upper_pipe_y = pipe_gap_y - self.pipe_height

            pygame.draw.rect(screen, self.color, (pipe_x, upper_pipe_y, self.pipe_width, self.pipe_height))

            # Lower pipe
            lower_pipe_y = pipe_gap_y + self.pipe_gap

            pygame.draw.rect(screen, self.color, (pipe_x, lower_pipe_y, self.pipe_width, self.pipe_height))

            self.collision()
            pipe_x -= self.speed


    def collision_x(self, pipe_x, bird_x, pipe_width):
        return pipe_x <= bird_x - 15 <= pipe_x + pipe_width or pipe_x <= bird_x + 15 <= pipe_x + pipe_width
    
    def collision_y(self, pipe_gap_y, bird_y, lower_pipe_y):
        return not (pipe_gap_y <= bird_y - 15 <= lower_pipe_y) or not (pipe_gap_y <= bird_y + 15 <= lower_pipe_y)


    def collision(self, pipe_x, bird_x, pipe_width, pipe_gap_y, bird_y, lower_pipe_y):
        return self.collision_x(pipe_x, bird_x, pipe_width) and self.collision_y(pipe_gap_y, bird_y, lower_pipe_y)
    

    # def track_score(self):
    #     if self.passed_pipe == False:
    #         if self.pipe_x + self.pipe_width/2 <= self.bird_x:
    #             self.score += 1
    #             self.passed_pipe = True
    #             print(self.score)

    def display_score(self):
        pass
