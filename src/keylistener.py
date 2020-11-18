

class KeyListener():
    
    KEY_COUNT = 320
    
    key = [False] * KEY_COUNT
    key_pressed = [False] * KEY_COUNT
    

    
    @classmethod
    def update(cls):
        for i in range(1,KeyListener.KEY_COUNT):
            KeyListener.key_pressed[i]=False
    
    
    @classmethod
    def update_key_down(cls,new_event):
        print(new_event.key)
        KeyListener.key[new_event.key] = True
        KeyListener.key_pressed[new_event.key] = True

   
    @classmethod
    def update_key_up(cls,new_event):
        KeyListener.key[new_event.key] = False

    

    