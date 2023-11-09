# THIS CODE IS DONE AS A PART OF THE COURSE "ADVANCED COMPUTER NETWORKS"
# BY Venu Pulagam (CB.EN.U4AIE21044)

import socket
import os

search_paths = [os.path.join(os.path.expanduser("~"), "Desktop"), 
                os.path.join(os.path.expanduser("~"), "Downloads"), "C:/", "D:/"]

# Add "E:/" if you want to search through the E drive

def search_file(filename, start_paths):
    for start_path in start_paths:
        for root, dirs, files in os.walk(start_path):
            if filename in files:
                return os.path.join(root, filename)
    return "REQUESTED FILE NOT FOUND"

def valid (filename) :
    if filename[len(filename)-4:len(filename)] == ".txt":
        out = 0
    else :
        out = 1
    return out

def GET(conn) :
    filename = conn.recv(1024).decode()
    print(filename)
    if filename[len(filename)-4:len(filename)] == ".txt" :
        file_path = search_file(filename, search_paths)
        
        if file_path == "REQUESTED FILE NOT FOUND" :
            feed = "REQUESTED FILE NOT FOUND !"
            conn.send(feed.encode())
        
        elif file_path != "REQUESTED FILE NOT FOUND" :
            print("REQUESTED FILE FOUND AT : " + file_path)
            with open(file_path, 'rb') as file:
                data = file.read(1024)
                while data:
                    conn.send(data)
                    data = file.read(1024)
                    feed = "REQUESTED FILE SENT SUCCESSFULLY !"
            conn.send(feed.encode())
               
    else :
        msg = "ERROR : Incorrect File Format"
        conn.send(msg.encode())
        print(msg + ", Connection closed")
        
def POST(conn) :
    filename = conn.recv(1024).decode()
    if valid(filename) == 0 :
        save_directory = os.path.join(os.path.expanduser("~"), "Downloads")
        path = os.path.join(save_directory, filename)
        print(f"Saving file to: {path}")
        
        feed = "New resource created succesfully !"
        print(feed)
        conn.send(feed.encode())
        
        with open(path, 'wb') as file:
            data = conn.recv(1024)
            while data:
                file.write(data)
                data = conn.recv(1024)
    else :
        feed = "ERROR : Incorrect File format !"
        print(feed)
        conn.send(feed.encode())
        
    
        
def PUT (conn) :
    ind = 0
    if ind == 0:
        ind = ind+1
        filename = conn.recv(1024).decode()
    print("TRYING TO UPDATE CONTENT IN : " + filename)
    val = valid(filename)
    
    if ind == 1:
        newcontent = conn.recv(1024).decode()
        ind = ind + 1
    
    print("UPDATE CONTENT WITH : " + newcontent)
    
    if val == 0 :
        file_path = search_file(filename, search_paths)
        if file_path != "REQUESTED FILE NOT FOUND" :
            feed = "Content replaced successfully !"
            conn.send(feed.encode())
        
            with open(file_path, 'w') as file:
                while newcontent:
                    file.write(newcontent)
                    newcontent = conn.recv(1024).decode()
                print(f"Content replaced successfully in {file_path}")
                
        elif file_path == "REQUESTED FILE NOT FOUND" :
            save_directory = os.path.join(os.path.expanduser("~"), "Downloads")
            path = os.path.join(save_directory, filename)
            
            feed = "REQUESTED FILE NOT FOUND, HENCE CREATED A NEW RESOURCE"
            print(feed)
            conn.send(feed.encode())
            
            with open(path, 'w') as file:
                while newcontent:
                    file.write(newcontent)
                    newcontent = conn.recv(1024).decode()
    else :
        feed = "ERROR : Incorrect file format !"
        print(feed)
        conn.send(feed.encode())
    
def DELETE (conn) :
    filename = conn.recv(1024).decode()
    if valid(filename) == 0 :
        path = search_file(filename, search_paths)
        if path != "REQUESTED FILE NOT FOUND" :
            print("Successfully deleted : " + path)
            os.remove(path)
            feed = "Deletion succesful !"
        else :
            feed = "REQUESTED FILE NOT FOUND"
        print(feed)
        conn.send(feed.encode())
    else :
        feed = "ERROR : Incorrect file format !"
        print(feed)
        conn.send(feed.encode())

def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
        
    op = conn.recv(1024).decode()
    print("NEW REQUEST : " + op)
    
    if op == "1":
        GET(conn)
    if op == "2":
        POST(conn)
    if op == "3":
        PUT(conn)
    if op == "4":
        DELETE(conn)

    conn.close()


server_program()