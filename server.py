#!python2
import socket

class TCPSever(object):
    def __init__(self):
        self.carrier_group_1 = []
        self.carrier_group_2 = []
        self.carrier_group_3 = []
        self.first_run = True

    def connectToClient(self):
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
            if (first_run == True):
                if (data == 1):
                    self.carrier_group_1.append(data)
                    print("initialization status: Sucessfull")
                elif(data == 2):
                    self.carrier_group_2.append(data)
                    print("initialization status: Sucessfull")
                elif(data == 3):
                    self.carrier_group_3.append(data)
                    print("initialization status: Sucessfull")
                else:
                    data = 0
                    print("initialization status: Failed..." )
                    c.send(data
                c.close()
            else:
                print "Received RFID Tag from PlC is: " + str(data)
                if (data in self.carrier_group_1):
                    data = 1
                elif(data == data in self.carrier_group_2):
                    data = 2
                elif(data in self.carrier_group_3):
                    data = 3
                else:
                    data = 0
                print("Sending back: " + str(data))
                c.send(data
                c.close()



if __name__ == '__main__':
    server = TCPSever()
    server.connectToClient()
