import pygame
import pygame.gfxdraw
import pymunk

class Player:
    def __init__(self, space, x, y):
        # for rendering
        self.radius = 12
        # blue color
        self.color = (0, 0, 255)
        self.max_health = 100
        self.health = self.max_health
        self.mass = 5.0
        
        # for physics
        moment = pymunk.moment_for_circle(
            self.mass,  # mass
            0,  # inner radius
            self.radius  # outer radius
        )
        
        self.body = pymunk.Body(self.mass, moment)
        self.body.position = (x, y)
        self.shape = pymunk.Circle(self.body, self.radius)
        
        space.add(self.body, self.shape)

    def update(self):
        # update based on arrow keys/WASD
        keys = pygame.key.get_pressed()
        force = pymunk.Vec2d(0, 0)

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            force += (-1, 0)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            force += (1, 0)
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            force += (0, -1)
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            force += (0, 1)
        if force.length > 0:
            force = force.normalized() * 15000

        self.body.apply_force_at_local_point(force, (0, 0))
        
        # friction
        self.body.velocity *= 0.95
    def change_color(self, color):
        self.color = color
        
    
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