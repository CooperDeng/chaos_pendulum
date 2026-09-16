import pymunk


class PhysicsWorld:
    def __init__(self):
        self.space = pymunk.Space()
        self.space.gravity = (0, 0)
        self.space.damping = 0.95

    def update(self, dt):
        self.space.step(dt)