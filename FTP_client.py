# THIS CODE IS DONE AS A PART OF THE COURSE "ADVANCED COMPUTER NETWORKS"
# BY Venu Pulagam (CB.EN.U4AIE21044)


# The files POSTED in the SERVER by the CLIENT will be stored in DOWNLOADS folder in the SERVER


import socket
import os

def client_program():
    host = socket.gethostname()
    port = 5000

    client_socket = socket.socket()
    client_socket.connect((host, port))

    filename = input("ENTER THE FILENAME : ")

    
    client_socket.send(filename.encode())
        
    yesno = client_socket.recv(1024)
        
    if yesno.decode() != "REQUESTED FILE NOT FOUND" and yesno.decode() != "Incorrect File Format":
        save_directory = os.path.join(os.path.expanduser("~"), "Downloads")
        path = os.path.join(save_directory, filename)
        print(f"Saving file to: {path}")
            
        with open(path, 'wb') as file:
            file.write(yesno)
            data = client_socket.recv(1024)
            while data:
                file.write(data)
                data = client_socket.recv(1024)
            print("FILE RECIEVED SUCCESFULLY !")
    elif yesno.decode() == "REQUESTED FILE NOT FOUND":
        print(yesno.decode())
    elif yesno.decode() == "Incorrect File Format":
        print(yesno.decode())
    
            
    client_socket.close()


if __name__ == '__main__':
    client_program()