import Model_Pygame
import pygame
import random

class Game_play:
    def __init__(self):
        self.speed = 20
        self.pipe_width = 45
        self.pipe_x = 720 # Change somehow
        self.pipe_height = 720
        self.pipe_gap = 100
        self.pipe_gap_y = 140

        self.bird_x = 200

        self.score = 0

        self.color = (0, 255, 6)
    
    def bird_hitbox(self, screen, model: Model_Pygame.Model):
        self.bird_y = model.get_y_pos() + 120
        pygame.draw.circle(screen, self.color, (self.bird_x, self.bird_y), 15) # Color OG: 0, 0, 6

    def pipe_hitboxes(self, screen):
        if self.pipe_x < -self.pipe_width: 
            self.pipe_x = 720 # Change
            self.pipe_gap_y = random.randint(140, 480 - self.pipe_gap - 20)
            self.passed_pipe = False

        # Upper pipe
        # pipe_x = screen.get_width()
        self.upper_pipe_y = self.pipe_gap_y - self.pipe_height

        pygame.draw.rect(screen, self.color, (self.pipe_x, self.upper_pipe_y, self.pipe_width, self.pipe_height))

        # Lower pipe
        self.lower_pipe_y = self.pipe_gap_y + self.pipe_gap

        pygame.draw.rect(screen, self.color, (self.pipe_x, self.lower_pipe_y, self.pipe_width, self.pipe_height))

        self.pipe_x -= self.speed


    def collision_x(self):
        return self.pipe_x <= self.bird_x - 15 <= self.pipe_x + self.pipe_width or self.pipe_x <= self.bird_x + 15 <= self.pipe_x + self.pipe_width
    
    def collision_y(self):
        return not (self.pipe_gap_y <= self.bird_y - 15 <= self.lower_pipe_y) or not (self.pipe_gap_y <= self.bird_y + 15 <= self.lower_pipe_y)


    def collision(self):
        return self.collision_x() and self.collision_y()
    

    def track_score(self):
        if self.passed_pipe == False:
            if self.pipe_x + self.pipe_width/2 <= self.bird_x:
                self.score += 1
                self.passed_pipe = True
                print(self.score)

    def display_score(self):
        pass