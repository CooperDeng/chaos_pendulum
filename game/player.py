import pygame
import pygame.gfxdraw

class Player:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.radius = 10
        self.color = (255, 255, 255)  # White color
        self.mass = 5 # in kg
        self.max_health = 100
        self.health = self.max_health
        self.velocity = pygame.Vector2(0, 0)

    def update(self, mouse_pos):
        self.position.x = mouse_pos[0]
        self.position.y = mouse_pos[1]

    def draw(self, screen):
        x = int(self.position.x)
        y = int(self.position.y)

        pygame.gfxdraw.aacircle(
            screen,
            x,
            y,
            self.radius,
            self.color
        )

        pygame.gfxdraw.filled_circle(
            screen,
            x,
            y,
            self.radius,
            self.color
        )