import socket
import sys
import io

def getFile (host, port, files):



    address = (host,int(port))

    request = "GET /%s HTTP/1.1\r\nHost:%s\r\n\r\n" % (files, host)

    print(request)

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(address)
    sock.settimeout(5)

    sock.send(request.encode("ascii"))

    binary = b''
    show = ''

    data = b'null'

    x=0
    while x < 4:

        aux = sock.recv(1).decode("ascii")
        show += aux
        
        if aux == '\n' or aux == '\r':
            x = x + 1
        else: 
            x = 0 

    if(files == ""):
        files = "index.html"    
    while data:
        try:
            data = sock.recv(1024)
        except:
            break
        binary += data
    with io.open(files, "wb") as f:
        f.write(binary)

        
    sock.close()    

    return show