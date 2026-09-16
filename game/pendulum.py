import math
import pygame


class Pendulum:
    def __init__ (self, pivot, draw_ball, draw_inter_ball=False, length=120, radius=14):
        self.pivot = pygame.Vector2(pivot)
        self.previous_pivot = pygame.Vector2(pivot)
        self.pivot_velocity = pygame.Vector2(0, 0)
        self.piviot_acceleration = pygame.Vector2(0, 0)
        
        self.draw_ball = draw_ball
        self.draw_inter_ball = draw_inter_ball

        self.length = length
        self.radius = radius

        self.angle = math.pi / 4 
        self.angular_velocity = 0
        self.angular_acceleration = 0
        
        self.ball_position = pygame.Vector2(
            self.pivot.x + self.length * math.sin(self.angle),
            self.pivot.y + self.length * math.cos(self.angle)
        )
        
        self.gravity = 500 # pixels per second squared

    def update(self, pivot, dt):
        # Calculating the pivot's velocity and acceleration
        new_pivot = pygame.Vector2(pivot)
        new_velocity = (new_pivot - self.previous_pivot) / dt
        self.piviot_acceleration = (new_velocity - self.pivot_velocity) / dt
        self.pivot_velocity = new_velocity

        # breaking down pivot acceleration into x and y
        ax = self.piviot_acceleration.x
        ay = self.piviot_acceleration.y
        
        # Update the pivot position
        self.pivot.update(pivot)
        
        
        
        # Gravity determines angular acceleration
        self.angular_acceleration = (
                -(self.gravity / self.length)
                * math.sin(self.angle)

                -(ax / self.length)
                * math.cos(self.angle)

                +(ay / self.length)
                * math.sin(self.angle)
        )
        
        # Update angular velocity and angle
        self.angular_velocity += (
            self.angular_acceleration * dt
        )
        
        self.angle += (
            self.angular_velocity * dt
        )
        
        self.ball_position.x = (
            self.pivot.x + (self.length * math.sin(self.angle))
        )

        self.ball_position.y = (
            self.pivot.y + (self.length * math.cos(self.angle))
        )

    def draw(self, screen):
        pygame.draw.line(
            screen,
            (200, 200, 200),
            self.pivot,
            self.ball_position,
            3
        )
        if self.draw_ball:
            pygame.draw.circle(
                screen,
                (255, 255, 255),
                self.ball_position,
                self.radius
            )
        elif self.draw_inter_ball:
            pygame.draw.circle(
                screen,
                (100, 100, 100),
                self.ball_position,
                self.radius/2
            )
        else:
            return