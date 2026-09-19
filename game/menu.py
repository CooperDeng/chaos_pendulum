import math
import pygame


class MainMenu:
    def __init__(self, screen):
        self.screen = screen

        self.title_font = pygame.font.SysFont(
            "menlo",
            64
        )

        self.button_font = pygame.font.SysFont(
            "menlo",
            28
        )

        self.title_color = (235, 235, 235)
        self.button_color = (150, 150, 160)
        self.hover_color = (255, 255, 255)

        self.play_rect = None
        self.exit_rect = None

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.play_rect and self.play_rect.collidepoint(event.pos):
                    return "play"

                if self.exit_rect and self.exit_rect.collidepoint(event.pos):
                    return "exit"

        return None

    def draw(self):
        width = self.screen.get_width()
        height = self.screen.get_height()

        time = pygame.time.get_ticks() / 1000.0

        title_offset = math.sin(time * 1.2) * 5
        play_offset = math.sin(time * 1.5 + 1) * 3
        exit_offset = math.sin(time * 1.5 + 2) * 3

        mouse_pos = pygame.mouse.get_pos()

        title = self.title_font.render(
            "CHAOS PENDULUM",
            True,
            self.title_color
        )

        title_rect = title.get_rect(
            center=(
                width / 2,
                height / 2 - 140 + title_offset
            )
        )

        play_color = self.button_color
        exit_color = self.button_color

        if self.play_rect and self.play_rect.collidepoint(mouse_pos):
            play_color = self.hover_color

        if self.exit_rect and self.exit_rect.collidepoint(mouse_pos):
            exit_color = self.hover_color

        play = self.button_font.render(
            "PLAY",
            True,
            play_color
        )

        exit_button = self.button_font.render(
            "EXIT",
            True,
            exit_color
        )

        self.play_rect = play.get_rect(
            center=(
                width / 2,
                height / 2 + 10 + play_offset
            )
        )

        self.exit_rect = exit_button.get_rect(
            center=(
                width / 2,
                height / 2 + 70 + exit_offset
            )
        )

        self.screen.blit(
            title,
            title_rect
        )

        self.screen.blit(
            play,
            self.play_rect
        )

        self.screen.blit(
            exit_button,
            self.exit_rect
        )