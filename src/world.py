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
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from box import Box
from tetromino import Tetromino
from Box2D import (b2PolygonShape, b2World)
import Box2D

"""
This is a simple example of building and running a simulation using Box2D. Here
we create a large ground box and a small dynamic box.

** NOTE **
There is no graphical output for this simple example, only text.
"""


game_display = None


class World():

    b2_game_world = None
    groundBody = None
    body = None
    box = None
    game_tetrominos = []

    def create_box(self, new_x, new_y, new_width, new_height,new_index):
        print(type(game_display))
        new_tetromino = Tetromino(self, self.game_display, new_x, new_y,new_index)
        self.game_tetrominos.append(new_tetromino)

    def __init__(self, new_display):
        self.b2_game_world = b2World()  # default gravity is (0,-10) and doSleep is True
        self.groundBody = self.b2_game_world.CreateStaticBody(position=(0, -50),
                                                              shapes=b2PolygonShape(
                                                                  box=(80, 10)),
                                                              )
        # Create a dynamic body at (0, 4)

        self.game_display = new_display


# Prepare for simulation. Typically we use a time step of 1/60 of a second
# (60Hz) and 6 velocity/2 position iterations. This provides a high quality
# simulation in most game scenarios.

    timeStep = 1.0 / 60
    vel_iters, pos_iters = 6, 2

    def update(self):
        # Instruct the world to perform a single step of simulation. It is
        # generally best to keep the time step and iterations fixed.
        self.b2_game_world.Step(self.timeStep, self.vel_iters, self.pos_iters)

    # Clear applied body forces. We didn't apply any forces, but you should
    # know about this function.
        self.b2_game_world.ClearForces()

    def draw(self):
        for t in self.game_tetrominos:
            t.draw()
