import pygame
import pygame.gfxdraw
import pymunk

class Enemy:
    def __init__(self, space, x, y):
        self.mass = 10
        self.radius = 20

        self.color = (200, 100, 100)
        self.max_health = 100
        self.health = self.max_health

        self.body = pymunk.Body(self.mass, pymunk.moment_for_circle(self.mass, 0, self.radius))
        self.body.position = (x, y)
        self.shape = pymunk.Circle(self.body, self.radius)

        space.add(self.body, self.shape)

    def update(self, target_position):
        # Enemies simply moves towards the player
        force = pymunk.Vec2d(0, 0)
        direction = target_position - self.body.position

        # Normalize the direction vector
        if direction.length > 0:
            direction = direction.normalized()

        force = direction * 300
        self.body.apply_force_at_local_point(force, (0, 0))

    def draw(self, screen):
        x = int(self.body.position.x)
        y = int(self.body.position.y)

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

    def death(self, space):
        space.remove(self.body, self.shape)