import pygame

from .physics import PhysicsWorld
from .player import Player
from .pendulum import PendulumChain
from .menu import MainMenu
from .enemy import Enemy
from .wall import Wall

class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()
        self.screen_width = 1920
        self.screen_height = 1080
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

        self.wall = Wall(
            self.physics_world.space,
            self.screen.get_width(),
            self.screen.get_height()
        )

        self.enemy_list = []

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

        self.state = "menu"  # Possible states: "menu", "game"
        self.menu = MainMenu(self.screen)
        
    def run(self):
        while self.running:
            # Cap the frame rate to 60
            self.dt = self.clock.tick(60) / 1000.0

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    
                if self.state == "menu":
                    result = self.menu.handle_event(event)
                    
                    if result == "play":
                        self.state = "game"
                    elif result == "exit":
                        self.running = False
            

            # Clear the screen
            self.screen.fill("black")
            if self.state == "menu":
                self.menu.draw()
            elif self.state == "game":

                # Enemy spawner 
                if len(self.enemy_list) < 5 and pygame.time.get_ticks() % 10000 == 0: # 10000 ms = 10 seconds
                    enemy = Enemy(
                        self.physics_world.space,
                        self.screen.get_width() * 0.1,
                        self.screen.get_height() * 0.1
                    )
                    self.enemy_list.append(enemy)

                # Update
                self.player.update()
                for enemy in self.enemy_list:
                    enemy.update(self.player.body.position)
                self.physics_world.update(self.dt)
                
                # Draw 
                self.player.draw(self.screen)
                for enemy in self.enemy_list:
                    enemy.draw(self.screen)
                self.pendulum.draw(self.screen)
                self.wall.draw(self.screen)
                


                # Update player health on top of screen as a really thin line
                player_health_ratio = self.player.health / self.player.max_health

                health_bar_height = 3

                pygame.draw.rect(
                    self.screen,
                    (255, 0, 0),
                    (0, self.screen_height - health_bar_height, self.screen.get_width() * player_health_ratio, 
                    health_bar_height)
                )


            # Update the display
            pygame.display.flip()

        pygame.quit()