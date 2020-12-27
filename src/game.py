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
from state import State
from world import World
from mouselistener import MouseListener
from keylistener import KeyListener

class Game(State):
    
    game_world = None
    current_index = -1
    
    def create_game_world(self):
        print(type(self.game_display))
        
        self.game_world = World(self.game_display)
    
    
    
    
    def draw(self):
        self.game_world.draw()
        
    def update(self):
        
        if MouseListener.button_pressed[MouseListener.Buttons.MOUSE_LEFT_CLICK.value]:
            self.game_world.create_box(MouseListener.mouse_x/20, -(MouseListener.mouse_y/20), 1.6, 1.6, self.current_index)
            self.current_index-=1
            
        if MouseListener.button_pressed[MouseListener.Buttons.MOUSE_RIGHT_CLICK.value]:
            self.game_world.create_box(MouseListener.mouse_x/20, -(MouseListener.mouse_y/20), 1, 1, self.current_index)
        
        if KeyListener.key_pressed[pygame.K_r]:
            self.game_world.create_box(MouseListener.mouse_x/20, -(MouseListener.mouse_y/20), 1.6, 1.6, self.current_index)
            
        if KeyListener.key[pygame.K_e]:
            self.game_world.create_box(MouseListener.mouse_x/20, -(MouseListener.mouse_y/20), 1.6, 1.6, self.current_index)

            
        self.game_world.update()

        
