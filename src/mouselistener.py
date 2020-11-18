
from enum import Enum
import pygame

class MouseListener:
    
    mouse_x=0
    mouse_y=0
    button = [False] * 6
    button_pressed = [False] * 6
    
    class Buttons(Enum):
        MOUSE_LEFT_CLICK = 1
        MOUSE_MIDDLE_CLICK = 2        
        MOUSE_RIGHT_CLICK = 3
        MOUSE_WHEEL_UP = 4
        MOUSE_WHEEL_DOWN = 5
        
    
    @classmethod
    def update(cls):
        for i in range(1,6):
            MouseListener.button_pressed[i]=False
    
    @classmethod
    def update_pos(cls,new_event):
        MouseListener.mouse_x = new_event.pos[0]
        MouseListener.mouse_y = new_event.pos[1]
    
    @classmethod
    def update_button_down(cls,new_event):
        MouseListener.button[new_event.button] = True
        MouseListener.button_pressed[new_event.button] = True

   
    @classmethod
    def update_button_up(cls,new_event):
        MouseListener.button[new_event.button] = False

