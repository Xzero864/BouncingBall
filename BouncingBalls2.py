import pygame
import random
from gameObjects.BallFactory import BallFactory

"""
BouncingBalls.py

Description:
This Python application simulates bouncing balls with physics-based gravity and collisions.
Users can interact with the simulation by freezing or flinging balls, and walls can be damaged
and destroyed by larger balls. Once walls break, a vacuum effect is triggered, pulling balls out of the area.

Author: [Jason]
Date: [9/26/24]

NOTE: ChatGPT was used throughout to generate header comments 
"""

class Game:
    def __init__(self):
        '''
        |                     |
        |   Pygame Setup      |
        |_____________________|
        '''
        pygame.init()
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Basic Ball Class")

        ''' 
        |                     |
        |   Color Definition  |
        |_____________________| 
        '''
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.GRAY = (200, 200, 200)
        self.YELLOW = (255, 255, 0)

        ''' 
        |                     |
        |   Game Setup        |
        |_____________________| 
        '''
        self.running = True
        self.clock = pygame.time.Clock()
        self.stars = self.create_stars()

        ''' 
        |                     |
        |   Ball Factories    |
        |_____________________| 
        '''
        self.blue_factory = BallFactory(screen_width=self.WIDTH, screen_height=self.HEIGHT, color=self.BLUE)
        self.red_factory = BallFactory(screen_width=self.WIDTH, screen_height=self.HEIGHT, color=self.RED)
        self.green_factory = BallFactory(screen_width=self.WIDTH, screen_height=self.HEIGHT, color=self.GREEN)
        self.yellow_factory = BallFactory(screen_width=self.WIDTH, screen_height=self.HEIGHT, color=self.YELLOW)

        ''' 
        |                     |
        |   Groups            |
        |_____________________| 
        '''
        self.blue_group = self.blue_factory.make_balls(4)
        self.red_group = self.red_factory.make_balls(4)
        self.green_group = self.green_factory.make_balls(4)
        self.yellow_group = self.yellow_factory.make_balls(4)
        self.groups = [
            self.blue_group,
            self.red_group,
            self.green_group,
            self.yellow_group

        ]

        self.walls = pygame.sprite.Group()

    ''' 
    |                     |
    |   Helper Methods    |
    |_____________________| 
    '''
    def create_stars(self):
        all_stars = []
        for _ in range(75):
            star_x = random.randint(0, self.WIDTH)
            star_y = random.randint(0, self.HEIGHT)
            all_stars.append((star_x, star_y))
        return all_stars

    def handle_collisions(self):
        balls_to_remove = set()

        for group1 in self.groups:
            for group2 in self.groups:
                # Intentionally checking against itself, different logic if group1 == group2
                print(group1)
                print(group2)
                collisions = pygame.sprite.groupcollide(group1, group2, False, False)
                for ball1, ball_list in collisions.items():
                    for ball2 in ball_list:
                        if ball1 != ball2:
                            if group1 == group2 and ball1 not in balls_to_remove and ball1.radius >= ball2.radius:
                                ball1.grow()
                                balls_to_remove.add(ball2)
                            else:
                                ball1.bounce()
                                ball2.bounce()

        for ball in balls_to_remove:
            for group in self.groups:
                if ball in group:
                    group.remove(ball)

    def update_balls(self):
        for group in self.groups:
            group.update()
            group.draw(self.screen)

    '''
    |                     |
    |   Main Game Loop    |
    |_____________________|
    '''
    def run(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Fill the screen with black
            self.screen.fill(self.BLACK)

            # Draw stars
            for star in self.stars:
                pygame.draw.circle(self.screen, self.YELLOW, star, 2)

            # Handle ball collisions and updates
            self.handle_collisions()
            self.update_balls()

            pygame.display.flip()
            self.clock.tick(60)

        # Quit Pygame
        pygame.quit()


# Initialize and run the game
if __name__ == "__main__":
    game = Game()
    game.run()
