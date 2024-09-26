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
"""


''' 
|                     |
|   Pygame Setup      |
|_____________________|
'''
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Basic Ball Class")


''' 
|                     |
|   Color Definition  |
|_____________________|
'''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (200, 200, 200)
YELLOW = (255, 255, 0)






def create_stars():
    all_stars = []
    for _ in range(75):
        star_x = random.randint(0, WIDTH)
        star_y = random.randint(0, HEIGHT)
        all_stars.append((star_x, star_y))
    return all_stars

''' 
|                     |
|   Constants         |
|_____________________|
'''

running = True
clock = pygame.time.Clock()
stars = create_stars()


''' 
|                     |
|   Ball Factories    |
|_____________________|
'''
blue_factory = BallFactory(screen_width=WIDTH, screen_height=HEIGHT, color=BLUE)
red_factory = BallFactory(screen_width=WIDTH, screen_height=HEIGHT, color=RED)
green_factory = BallFactory(screen_width=WIDTH, screen_height=HEIGHT, color=GREEN)
yellow_factory = BallFactory(screen_width=WIDTH, screen_height=HEIGHT, color=YELLOW)


''' 
|                     |
|   Groups            |
|_____________________|
'''
groups = [
    blue_group := blue_factory.make_balls(4),
    red_group := red_factory.make_balls(4),
    green_group := green_factory.make_balls(4),
    yellow_group := yellow_factory.make_balls(4),
]
walls = pygame.sprite.Group()

''' 
|                     |
|   Main Game Loop    |
|_____________________|
'''

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with white
    screen.fill(BLACK)

    # Make stars
    for star in stars:
        pygame.draw.circle(screen, YELLOW, star, 2)

    balls_to_remove = set()

    for group1 in groups:
        for group2 in groups:
            # Intentionally checking against itself, different logic if group1 == group2
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
        for group in groups:
            if ball in group:
                group.remove(ball)

    for group in groups:
        group.update()
        group.draw(screen)



    pygame.display.flip()


    clock.tick(60)

# Quit Pygame
pygame.quit()
