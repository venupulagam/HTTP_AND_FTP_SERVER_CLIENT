# HTTP_AND_FTP_SERVER_CLIENT
 Implementation of two well known protocols HTTP (Hyper Text Transfer Protocol) and FTP (File Transfer Protocol) has been done with the client-server communication model in Python, as a part of the course Advanced computer networks.

FTP :

When the client requests a file:
a. If the requested file is available with the server, the server should send back the requested file
to the client.
b. If the requested file is not available with the server, the server should send an error message
to the client saying “Requested File Not Found”.
c. If the requested file has an incorrect extension, the server should communicate “Incorrect File
Format” to the client.

Note: Use .txt as the valid extension for the files communicated.

HTTP :

a. GET: The contents of the requested resource should be displayed in the client. If the requested
resource is not available with the server, the server should communicate an error message to
the client.
b. POST: The server should create a new resource corresponding to the data communicated by
the client.
c. PUT: Client communicates the name of the resource to be updated, along with the updated
content. The server updates the content of the said resource accordingly. If the said resource
is not available with the server, the server creates a new resource with the updated content.
d. DELETE: Client communicates the name of the resource to be deleted in the server. The server
performs the deletion accordingly. If the corresponding resource is not present in the server,
an error message should be communicated to the client.

Note: You may use files as resources, i.e., modify the code of FTP to include the above
functionalities.