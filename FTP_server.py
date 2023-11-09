# THIS CODE IS DONE AS A PART OF THE COURSE "ADVANCED COMPUTER NETWORKS"
# BY Venu Pulagam (CB.EN.U4AIE21044)

import socket
import os

search_paths = [
    os.path.join(os.path.expanduser("~"), "Desktop"),
    os.path.join(os.path.expanduser("~"), "Downloads"),
    "C:/", "D:/"] 

# Add "E:/" if you want to search through the E drive

def search_file(filename, start_paths):
    for start_path in start_paths:
        for root, dirs, files in os.walk(start_path):
            if filename in files:
                return os.path.join(root, filename)
    return "REQUESTED FILE NOT FOUND"

def server_program():
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))
        
    filename = conn.recv(1024).decode()
    if filename[len(filename)-4:len(filename)] == ".txt" :
        file_path = search_file(filename, search_paths)
    
        print("REQUEST RECIEVED, SEARCHING FOR : " + str(filename))
        
        if file_path == "REQUESTED FILE NOT FOUND" :
            conn.send("REQUESTED FILE NOT FOUND".encode())
        
        elif file_path != "REQUESTED FILE NOT FOUND" :
            print("REQUESTED FILE FOUND AT : " + file_path)
            with open(file_path, 'rb') as file:
                data = file.read(1024)
                while data:
                    conn.send(data)
                    data = file.read(1024)
                print("REQUESTED FILE SENT SUCCESSFULLY !")
    else :
        msg = "Incorrect File Format"
        conn.send(msg.encode())
        print(msg + ", Connection closed")

    conn.close()

if __name__ == '__main__':
    server_program()