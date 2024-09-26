import pygame
import random

"""
Ball.py

Description:
This module defines the Ball class, which extends pygame's Sprite class to represent a ball in the game. Each ball has 
its own position, velocity, size (radius), and color. Balls move within the boundaries of the screen, bounce off the edges, 
and can interact by bouncing off each other or growing when they collide with same-colored balls.

Classes:
- Ball: A pygame sprite that represents a ball, which can move, bounce, and grow.

Methods:
- __init__(radius, color, screen_width, screen_height): Initializes the ball with specified radius, color, and screen boundaries.
- update(): Updates the ball’s position and handles bouncing off screen edges.
- bounce(): Changes the ball’s direction and speed when it collides with another ball of a different color.
- grow(): Increases the size of the ball when it merges with another ball of the same color.

Usage:
- Instantiate Ball objects with a radius, color, screen width, and screen height.
- Use the update method to animate the ball.
- Use the bounce and grow methods for interactions between balls.

Author: [Jason Silva]
Date: [9/24]
"""

class Ball(pygame.sprite.Sprite):
    def __init__(self, radius, color, screen_width, screen_height):
        '''
        Nothing
        :param radius: the radius of the ball
        :param color: the color of the ball
        :param screen_width: screen_width
        :param screen_height: screen_height
        '''
        super().__init__()
        self.x = screen_width / random.uniform(1,5)
        self.y = screen_height / random.uniform(1,5)
        self.radius = radius
        self.color = color
        self.image = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.speed_x = random.uniform(-5, 5)
        self.speed_y = random.uniform(-5, 5)
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.is_frozen = False


    def update(self):
        if self.is_frozen:
            return


        # Bounce off the walls
        if self.rect.left < 0:
            self.rect.left = 0
            self.speed_x = abs(self.speed_x) + random.uniform(-1, 1)
        elif self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
            self.speed_x = -abs(self.speed_x) + random.uniform(-1, 1)

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed_y = abs(self.speed_y) + random.uniform(-1, 1)
        elif self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
            self.speed_y = -abs(self.speed_y) + random.uniform(-1, 1)

        if abs(self.speed_x) < 1:
            self.speed_x = 1 if self.speed_x >= 0 else -1
        if abs(self.speed_y) < 1:
            self.speed_y = 1 if self.speed_y >= 0 else -1
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def bounce(self):
        '''
        Bounces two balls off of eachother when balls of different types collide
        :return: nothing
        '''

        self.speed_x = -self.speed_x + random.uniform(-1, 1)
        self.speed_y = -self.speed_y + random.uniform(-1, 1)


        self.speed_x = max(min(self.speed_x, 7), -7)
        self.speed_y = max(min(self.speed_y, 7), -7)


    def grow(self):
        '''
        Grows the balls when two balls of the same color collide
        :return: nothing
        '''
        current_center = self.rect.center
        self.radius *= 2
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
        self.rect = self.image.get_rect(center=current_center)