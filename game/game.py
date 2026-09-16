import pygame
from .player import Player
from .pendulum import Pendulum

class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.player = Player(self.screen.get_width() / 2, self.screen.get_height() / 2)
        # pendulum_one is the first pendulum, pendulum_two is the second pendulum
        self.pendulum_one = Pendulum((self.screen.get_width() / 2, self.screen.get_height() / 2), draw_ball=False, draw_inter_ball=True)
        self.pendulum_two = Pendulum(self.pendulum_one.ball_position, draw_ball=True, draw_inter_ball=False)
        
        self.dt = 0
        self.gravity = 500 # pixels per second squared

    def run(self):
        while self.running:
            # Cap the frame rate to 60
            self.dt = self.clock.tick(60) / 1000.0
                        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update player position
            self.player.update([self.screen.get_width() / 2, self.screen.get_height() / 2])
            #self.player.update(pygame.mouse.get_pos())
            
            # Update pendulums position
            self.pendulum_one.update(self.player.position, self.dt)
            self.pendulum_two.update(self.pendulum_one.ball_position, self.dt)

            # Clear the screen
            self.screen.fill("black")
            
            # Draw the player as a circle
            self.player.draw(self.screen)

            # Draw the pendulums
            self.pendulum_one.draw(self.screen)
            self.pendulum_two.draw(self.screen)

            # Update the display
            pygame.display.flip()

            

        pygame.quit()