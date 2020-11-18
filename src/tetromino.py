import pygame
from box import Box
"""
------------------------------------------------------------------------
[program description]
------------------------------------------------------------------------
Author: Danny Van Stemp
ID:     181549810
Email:  whatsmyemail@idunno.ca
__updated__ = "2018-07-27"
------------------------------------------------------------------------
"""

import pygame


class Tetromino(object):

    game_sprite = pygame.image.load("src/box.png")

    body = None
    game_display = None
    boxes = []
    height = 0.0
    width = 0.0
    shape = [(0, 0), (0, 1), (1, 0), (2, 0)]

    def rot_center(self, image, angle):
        """rotate an image while keeping its center and size"""
        loc = image.get_rect().center  # rot_image is not defined
        rot_sprite = pygame.transform.rotate(image, angle)
        rot_sprite.get_rect().center = loc
        return rot_sprite

    def __init__(self, new_world, new_display, new_x, new_y):
        for cell in self.shape:
            box = Box(new_world, new_display, new_x +
                      cell[0], new_y+cell[1], 1.6, 1.6)
            self.boxes.append(box)

    def draw(self):

        for box in self.boxes:
            box.draw()
