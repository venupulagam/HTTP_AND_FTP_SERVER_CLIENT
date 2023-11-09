# THIS CODE IS DONE AS A PART OF THE COURSE "ADVANCED COMPUTER NETWORKS"
# BY Venu Pulagam (CB.EN.U4AIE21044)

import socket
import os

# FOR EASE OF CHECKING THE CODE, PLEASE OPERATE ON FILES ON THE DESKTOP
# ELSE IT WOULD TAKE LONGER AS THE FILE SHOULD BE SEARCHED FOR, IN ALL THE EXISTING PATHS

def GET (filename, client_socket):
    client_socket.send(filename.encode())
    yesno = client_socket.recv(1024)
    
    if yesno.decode() != "REQUESTED FILE NOT FOUND" and yesno.decode() != "Incorrect File Format":
        print(yesno.decode())
        data = client_socket.recv(1024).decode()
        print(data)
        while data :    
            data = client_socket.recv(1024).decode()
        feed = client_socket.recv(1024).decode()
        print(feed)
        
    elif yesno.decode() == "REQUESTED FILE NOT FOUND":
        print(yesno.decode())
    elif yesno.decode() == "Incorrect File Format":
        print(yesno.decode())
        
def POST(filename, data, client_socket):
    client_socket.send(filename.encode())
    feed = client_socket.recv(1024).decode()
    client_socket.send(data.encode())
    print(feed)

    
def PUT(filename, newcontent, client_socket):
    ind = 0
    if ind == 0:
        client_socket.send(filename.encode())
        ind = ind + 1
    if ind == 1 :
        client_socket.send(newcontent.encode())
        ind = ind + 1
    feed = client_socket.recv(1024).decode()
    print(feed)
        
    
def DELETE(filename, client_socket):
    client_socket.send(filename.encode())
    feed = client_socket.recv(1024).decode()
    print(feed)

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))        
        
    print("Connection to HTTP SERVER established successfully ! ")
    print("Choose one action")
    print("1. GET")
    print("2. POST")
    print("3. PUT")
    print("4. DELETE")
    
    op = input("Enter the index of the required operation : ")
    
    client_socket.send(op.encode())
    
    if op == "1" :
        filename = input("Enter a valid filename (.txt) : ")
        GET(filename, client_socket)
    elif op == "2":
        filename = input("Enter a valid filename (.txt) : ")
        data = input("Enter the data you want to write into this new file : ")
        POST(filename, data, client_socket)
    elif op == "3":
        filename = input("Enter a valid filename (.txt) : ")
        newcontent = input("Enter the updated content : ")
        PUT(filename, newcontent, client_socket)
    elif op == "4":
        filename = input("Enter a valid filename (.txt) : ")
        DELETE(filename, client_socket)
            
            
    client_socket.close()


if __name__ == '__main__':
    client_program()