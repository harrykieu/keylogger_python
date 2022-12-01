from pynput import keyboard 

def on_press(key):
    if key == keyboard.Key.esc:
        listener.stop()
    
    
def on_release(key):
    try:
        '''with open("key.txt",'a+') as f:
            f.write(key.char)
            f.close()'''
        print(key.char,end='',flush=True)
    except AttributeError:
        pass

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
