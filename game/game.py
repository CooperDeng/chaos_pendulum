import pygame

from .physics import PhysicsWorld
from .player import Player
from .pendulum import PendulumChain


class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        self.screen_width = 1280
        self.screen_height = 720
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.dt = 0

        self.physics_world = PhysicsWorld()

        self.player = Player(
            self.physics_world.space,
            self.screen.get_width() / 2,
            self.screen.get_height() / 2
        )

        self.pendulum = PendulumChain(
            self.physics_world.space,
            self.player.body
        )

        self.pendulum.add_link(
            (
                self.player.body.position.x + 60,
                self.player.body.position.y
            ),
            mass=3.0,
            radius=10
        )

        self.pendulum.add_link(
            (
                self.player.body.position.x + 240,
                self.player.body.position.y
            ),
            mass=7.0,
            radius=16
        )

    def run(self):
        while self.running:
            # Cap the frame rate to 60
            self.dt = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update player position
            self.player.update()

            self.physics_world.update(self.dt)

            # Clear the screen
            self.screen.fill("black")

            # Draw the player as a circle
            self.player.draw(self.screen)

            self.pendulum.draw(self.screen)

            # Update the display
            pygame.display.flip()

        pygame.quit()