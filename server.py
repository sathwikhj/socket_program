import socket
import threading

HEADER=64
PORT=5067
FORMAT='utf-8'
DISCONNECT="!DISCONNECT"
SERVER=socket.gethostbyname(socket.gethostname())
ADDR=(SERVER,PORT)
print(socket.gethostname())
server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"[NEW CONNECTION] {addr} connected")
    connected=True
    while connected:
        msg_length=conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg=conn.recv(int(msg_length)).decode(FORMAT)
            if msg=="!DISCONNECT":
                connected=False
                print(f"[{addr}] {msg}")
            #conn.send("Message recieved".encode(FORMAT))
            try: 
                with open(msg,'rb') as file:
                    file_data=file.read()
                    conn.send(file_data)
                    print("File sent")
                pass
            except IOError:
                conn.send("Invalid Filename".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr= server.accept()
        thread=threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count()-1}")


print("Server is now listening...")

start()
