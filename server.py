#!python2
import socket

class TCPSever(object):
    def __init__(self):
        self.carrier_group_1 = []
        self.carrier_group_2 = []
        self.carrier_group_3 = []
        self.first_run = True
        self.host = '172.20.40.46'#'127.0.0.1'
        self.port = 5000

    def initCarriers(self):
        s = socket.socket()
        s.bind((self.host,self.port))

        s.listen(1)
        c, addr = s.accept()
        print "Successfully established connection from: " + str(addr)
        while (first_run == True):
            data = c.recv(1024)
            if not data:
                print "Failed to receive data from PLC."
                break
            if (data in self.carrier_group_1 == True and data in self.carrier_group_2 == True and data in self.carrier_group_3 == True):
                c.close()
                self.first_run = False
            if (data in self.carrier_group_1 == False):
                self.carrier_group_1.append(data)
            elif (data in self.carrier_group_2 == False):
                self.carrier_group_2.append(data)
            elif (data in self.carrier_group_3 == False):
                self.carrier_group_3.append(data)
            else:
                data = 0
                print("initialization status: Failed..." )
                c.send(data)
                c.close()
                self.first_run = False

    def connectToClient(self):
        s = socket.socket()
        s.bind((self.host,self.port))

        s.listen(1)
        c, addr = s.accept()
        print "Successfully established connection from: " + str(addr)
        while True:
            data = c.recv(1024)
            if not data:
                print "Failed to receive data from PLC."
                break
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
                c.send(data)
        c.close()



if __name__ == '__main__':
    server = TCPSever()
    server.initCarriers()
    server.connectToClient()
