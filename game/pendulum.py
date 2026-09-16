import pygame
import pymunk


class PendulumLink:
    def __init__(self, space, position, mass=5.0, radius=14):
        self.radius = radius
        self.mass = mass
        self.color = (255, 255, 255)

        moment = pymunk.moment_for_circle(
            self.mass,
            0,
            self.radius
        )

        self.body = pymunk.Body(
            self.mass,
            moment
        )

        self.body.position = position

        self.shape = pymunk.Circle(
            self.body,
            self.radius
        )

        space.add(
            self.body,
            self.shape
        )

    def draw(self, screen):
        x = int(self.body.position.x)
        y = int(self.body.position.y)

        pygame.draw.circle(
            screen,
            self.color,
            (x, y),
            self.radius
        )


class PendulumChain:
    def __init__(self, space, pivot_body):
        self.space = space
        self.pivot_body = pivot_body

        self.links = []
        self.joints = []

    def add_link(self, position, mass=5.0, radius=14):
        link = PendulumLink(
            self.space,
            position,
            mass,
            radius
        )

        if len(self.links) == 0:
            previous_body = self.pivot_body
        else:
            previous_body = self.links[-1].body

        joint = pymunk.PinJoint(
            previous_body,
            link.body
        )

        self.space.add(joint)

        self.links.append(link)
        self.joints.append(joint)

    def draw(self, screen):
        previous_position = self.pivot_body.position

        for link in self.links:
            current_position = link.body.position

            pygame.draw.line(
                screen,
                (200, 200, 200),
                (
                    int(previous_position.x),
                    int(previous_position.y)
                ),
                (
                    int(current_position.x),
                    int(current_position.y)
                ),
                3
            )

            link.draw(screen)

            previous_position = current_position