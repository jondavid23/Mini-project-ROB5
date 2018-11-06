#!python2
import socket

def Main():
    host = '192.168.0.2'#'127.0.0.1'
    port = 5000

    s = socket.socket()
    s.bind((host,port))

    s.listen(1)
    c, addr = s.accept()
    print "Successfully established connection from: " + str(addr)
    while True:
        data = c.recv(1024)
        if not data:
            print "Failed to receive data from PLC."
            break
        print "Received RFID Tag from PlC is: " + str(data)
        if (data == 1):
            data = 1
        elif(data == 2):
            data = 2
        elif(data == 3):
            data = 3
        else:
            data = "No tag received"
        print("Sending back: " + str(data))
        c.send(data
    c.close()

if __name__ == '__main__':
    Main()
