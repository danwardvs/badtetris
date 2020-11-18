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


class Box(object):

    game_sprite = pygame.image.load("src/box.png")

    body = None
    game_display = None
    box = None
    height = 0.0
    width = 0.0

    def rot_center(self, image, angle):
        """rotate an image while keeping its center and size"""
        loc = image.get_rect().center  # rot_image is not defined
        rot_sprite = pygame.transform.rotate(image, angle)
        rot_sprite.get_rect().center = loc
        return rot_sprite

    def __init__(self, new_world, new_display, new_x, new_y, new_width, new_height):
        self.game_display = new_display
        self.body = new_world.b2_game_world.CreateDynamicBody(
            position=(new_x, new_y))
        self.width = new_width
        self.height = new_height

    # And add a box fixture onto it (with a nonzero density, so it will move)
        self.box = self.body.CreatePolygonFixture(
            box=(new_width/2, new_height/2), density=1, friction=0.3)

    def draw(self):

        new_sprite = self.rot_center(
            self.game_sprite, self.body.angle*180/3.14)

        self.game_display.blit(new_sprite, (20*(self.body.position.x)-self.width *
                                            10, -20*(self.body.position.y)-self.height*10), new_sprite.get_rect())
        # pygame.draw.rect(self.game_display,(0,0,255),[20*(self.body.position.x)-self.width*10,-20*(self.body.position.y)-self.height*10,self.width*20,self.height*20],1)
