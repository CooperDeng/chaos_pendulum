import pygame
import pygame.gfxdraw
import pymunk

class Wall:
    def __init__(self, space, width, height):
        self.width = width
        self.height = height
        self.color = (100, 100, 100)

        self.left_segment = pymunk.Segment(space.static_body, (0, 0), (0, height), 1)
        self.right_segment = pymunk.Segment(space.static_body, (width, 0), (width, height), 1)
        self.top_segment = pymunk.Segment(space.static_body, (0, 0), (width, 0), 1)
        self.bottom_segment = pymunk.Segment(space.static_body, (0, height), (width, height), 1)

        for segment in [self.left_segment, self.right_segment, self.top_segment, self.bottom_segment]:
            segment.elasticity = 0.85
            segment.friction = 0.5

        space.add(self.left_segment, self.right_segment, self.top_segment, self.bottom_segment)

    def draw(self, screen):
        pygame.gfxdraw.line(screen, 0, 0, 0, self.height, self.color)  # Left wall
        pygame.gfxdraw.line(screen, self.width, 0, self.width, self.height, self.color)  # Right wall
        pygame.gfxdraw.line(screen, 0, 0, self.width, 0, self.color)  # Top wall
        pygame.gfxdraw.line(screen, 0, self.height, self.width, self.height, self.color)  # Bottom wall

    def __del__(self):
        # Ensure that the segments are removed from the space when the wall is deleted
        print("Deleting wall")
        if self.left_segment and self.right_segment and self.top_segment and self.bottom_segment:
            self.left_segment.space.remove(self.left_segment)
            self.right_segment.space.remove(self.right_segment)
            self.top_segment.space.remove(self.top_segment)
            self.bottom_segment.space.remove(self.bottom_segment)