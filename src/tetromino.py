import pygame
import Box2D
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

    body = None
    game_display = None
    boxes = []
    height = 0.0
    width = 0.0
    shapes = [[ (0, 1), (1, 0), (2, 0)],[ (1,0 ), (2, 0), (3, 0)],[ (0,-1 ), (0, 1), (1, 0)],[ (1,0 ), (1, 1), (0, 1)]]


    SEPERATION=1.63

    def rot_center(self, image, angle):
        """rotate an image while keeping its center and size"""
        loc = image.get_rect().center  # rot_image is not defined
        rot_sprite = pygame.transform.rotate(image, angle)
        rot_sprite.get_rect().center = loc
        return rot_sprite

    def __init__(self, new_world, new_display, new_x, new_y,new_index,new_type):
        box_base = Box(new_world, new_display, new_x, new_y, 1.6, 1.6,new_index,new_type)
        self.boxes.append(box_base)

        shape = self.shapes[new_type]
        for pos in shape:
            box_add = Box(new_world, new_display, new_x, new_y, 1.6, 1.6,new_index,new_type)
            rd = Box2D.b2WeldJointDef(
                bodyA=box_base.body,
                bodyB=box_add.body,
                localAnchorA=(pos[0]*self.SEPERATION, pos[1] * self.SEPERATION),  
            )
            new_world.b2_game_world.CreateJoint(rd)
            self.boxes.append(box_add)



    def draw(self):

        for box in self.boxes:
            box.draw()
