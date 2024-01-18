import Model_Pygame
import pygame
import random

class Game_play:
    def __init__(self, pipe_nums, screen: pygame.surface.Surface):
        self.pipe_width = 45
        self.pipe_height = 720
        self.pipe_gap = 100
        self.pipe_nums = pipe_nums
        self.speed = 20 - self.pipe_nums
        self.bird_x = 200
        self.num_resetted = 0
        self.pipe_x_list = []
        self.pipe_gap_y_list = []
        self.passed_pipe_list = []
        self.is_alive = True

        self.score = 0

        self.color = (0, 255, 6)

        self.passed_pipes = 0
        self.screen = screen
    
    def bird_hitbox(self, model: Model_Pygame.Model):
        self.bird_y = model.get_y_pos() + 120
        # pygame.draw.circle(self.screen, self.color, (self.bird_x, self.bird_y), 15) # 

    def bird_skin(self, bird_skin):
        bird_skin = pygame.image.load(bird_skin)
        bird_skin = pygame.transform.scale(bird_skin, (30, 30))
        self.screen.blit(bird_skin, (self.bird_x - 15, self.bird_y - 15))
        

    def pipe_hitboxes(self):
        for i in range(0, self.pipe_nums + 1): # For every pipe
            # Initialize pipe coordinates on startup
            if self.num_resetted <= self.pipe_nums:
                pipe_gap_y = random.randint(140, 480 - self.pipe_gap - 20)
                pipe_x = 720 + self.pipe_width * i + 720/(self.pipe_nums + 1) * i #figure out a way to run this only once
                self.num_resetted += 1
                passed_pipe = False
                self.pipe_x_list.append(pipe_x)
                self.pipe_gap_y_list.append(pipe_gap_y)
                self.passed_pipe_list.append(passed_pipe)

            pipe_x = self.pipe_x_list[i]

            # If pipe goes offscreen
            if pipe_x < -self.pipe_width: 
                pipe_x += 720 + (self.pipe_width + 1) * (self.pipe_nums + 1)
                pipe_gap_y = random.randint(140, 480 - self.pipe_gap - 20)
                self.pipe_gap_y_list[i] = pipe_gap_y
                self.passed_pipe_list[i] = False

            pipe_gap_y = self.pipe_gap_y_list[i]
            passed_pipe = self.passed_pipe_list[i]

            # Upper pipe
            upper_pipe_y = pipe_gap_y - self.pipe_height

            pygame.draw.rect(self.screen, self.color, (pipe_x, upper_pipe_y, self.pipe_width, self.pipe_height))

            # Lower pipe
            lower_pipe_y = pipe_gap_y + self.pipe_gap

            pygame.draw.rect(self.screen, self.color, (pipe_x, lower_pipe_y, self.pipe_width, self.pipe_height))

            
            if self.collision(pipe_x, self.bird_x, self.pipe_width, pipe_gap_y, self.bird_y, lower_pipe_y):
                self.is_alive = False
            pipe_x -= self.speed
            self.pipe_x_list[i] = pipe_x

            self.track_score(pipe_x, self.bird_x, self.pipe_width, passed_pipe, i)

    def check_if_alive(self):
        return self.is_alive


    def collision_x(self, pipe_x, bird_x, pipe_width):
        return pipe_x <= bird_x - 15 <= pipe_x + pipe_width or pipe_x <= bird_x + 15 <= pipe_x + pipe_width
    
    def collision_y(self, pipe_gap_y, bird_y, lower_pipe_y):
        return not (pipe_gap_y <= bird_y - 15 <= lower_pipe_y) or not (pipe_gap_y <= bird_y + 15 <= lower_pipe_y)


    def collision(self, pipe_x, bird_x, pipe_width, pipe_gap_y, bird_y, lower_pipe_y):
        return self.collision_x(pipe_x, bird_x, pipe_width) and self.collision_y(pipe_gap_y, bird_y, lower_pipe_y)
    
    def track_score(self, pipe_x, bird_x, pipe_width, passed_pipe, i):
        if not passed_pipe and pipe_x + pipe_width < bird_x:
            self.score += 1
            self.passed_pipe_list[i] = True

    def get_score(self):
        return self.score
    

    # def track_score(self):
    #     if self.passed_pipe == False:
    #         if self.pipe_x + self.pipe_width/2 <= self.bird_x:
    #             self.score += 1
    #             self.passed_pipe = True
    #             print(self.score)

    def display_score(self):
        pass
