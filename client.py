import socket
HEADER=64
PORT=5050 #sample port number
FORMAT='utf-8'
DISCONNECT="!DISCONNECT"
SERVER="" #enter server ip address
ADDR=(SERVER,PORT)
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)


def send():
    msg=input(str("Enter the file name to recieve: ")) #get filename
    message=msg.encode(FORMAT) #encode message
    msg_length=len(message) #get filename length
    send_len=str(msg_length).encode(FORMAT) #encoding str_len
    send_len+=b' '*(HEADER-len(send_len)) #padding
    client.send(send_len) #send length
    client.send(message) #send message
    data=client.recv(2048) #recieve file
    invalid=1
    while invalid:
        if(data.decode(FORMAT)=="Invalid Filename"):
            print("Invalid Filename")
            msg=input(str("Enter a valid filename: "))
            message=msg.encode(FORMAT)
            msg_length=len(message)
            send_len=str(msg_length).encode(FORMAT)
            send_len+=b' '*(HEADER-len(send_len))
            client.send(send_len)
            client.send(message)
            data=client.recv(2048)
        else:
            invalid=0
    filename=input("Enter the name of file: ")
    file=open(filename,'wb')#write bytes
    file.write(data)
    file.close()
    print("File recieved")

    message=DISCONNECT.encode(FORMAT) #encode message
    msg_length=len(message) #get filename length
    send_len=str(msg_length).encode(FORMAT) #encoding str_len
    send_len+=b' '*(HEADER-len(send_len)) #padding
    client.send(send_len) #send length
    client.send(message) #send message


send()
client.close()
#send(DISCONNECT)
