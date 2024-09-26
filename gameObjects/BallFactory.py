import pygame
from .Ball import Ball


"""
BallFactory.py

Description:
This module defines the BallFactory class, which is responsible for creating and grouping balls of the same color.
The factory generates a specified number of balls and returns them in a pygame sprite group, making it easy to
manage and interact with sets of balls in the game.

Classes:
- BallFactory: A class that generates a group of balls of the same color, each confined within the screen boundaries.

Methods:
- make_balls(num_balls: int) -> pygame.sprite.Group: Creates a specified number of Ball objects and adds them to a sprite group.

Usage:
- Instantiate BallFactory with screen dimensions and a color.
- Call make_balls() to generate a group of balls for use in the game.

Author: [Jason Silva]
Date: [9/26/24]
"""

class BallFactory:
    '''
    Meant to be used as a way of grouping same colored balls
    '''

    def __init__(self,screen_width, screen_height,color):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.color = color



    def make_balls(self, num_balls:int) -> pygame.sprite.Group:
        '''

        :param num_balls: Number of balls to create
        :return: A sprite group, with all of the balls in it
        '''
        group = pygame.sprite.Group()
        for _ in range(num_balls):
            new_ball = Ball(10, self.color,self.screen_width, self.screen_height)
            group.add(new_ball)

        return group
