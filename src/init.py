
from state import State

class Init(State):
    
    def __init__(self):
        print('tubbz')
    
    def draw(self):
        print("Nothign to draw here sir")
        
    def update(self):
        self.next_state=State.program_states.STATE_GAME.value