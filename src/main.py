
from keylistener import KeyListener
from mouselistener import MouseListener
from game import Game
from init import Init
from menu import Menu
from state import State
import pygame

game_display = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption('Nice Window')
pygame.display.flip()


current_state = Init()

clock = pygame.time.Clock()

running = True


def change_state(new_state):
    global current_state

    if new_state != State.program_states.STATE_NULL:
        if new_state == State.program_states.STATE_MENU.value:
            current_state = Menu()

        if new_state == State.program_states.STATE_GAME.value:
            current_state = Game()
            current_state.set_display(game_display)
            current_state.create_game_world()


while running:

    clock.tick(60)

    change_state(current_state.get_next_state())

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEMOTION:
            MouseListener.update_pos(event)

        elif event.type == pygame.MOUSEBUTTONUP:
            MouseListener.update_button_up(event)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            MouseListener.update_button_down(event)

        elif event.type == pygame.KEYDOWN:
            KeyListener.update_key_down(event)

        elif event.type == pygame.KEYUP:
            KeyListener.update_key_up(event)

    current_state.update()

    MouseListener.update()
    KeyListener.update()

    game_display.fill((255, 255, 255))

    current_state.draw()

    pygame.display.update()
