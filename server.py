# Echo server program

#!/usr/bin/env python3

import socket
import time
from random import randint

HOST = '172.20.40.46'                 # Symbolic name meaning all available interfaces
PORT = 65432              # Arbitrary non-privileged port

blue = []
green = []
black = []

# next = 1
# Create a socket with IPv4 and TCP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen(1)
    print('Waiting for client...')
    conn, addr = s.accept() # accept blocks and waits for an incoming connection
    with conn:
        print('Connected by: ', addr)
        start = time.time()
        while True:
            now = time.time()
            if (now - start) >= 50000:
                print('Connection timed out...')
                break
            data = conn.recv(1024)
            if not data:
                #print('No data')
                continue

            # Check if the carrier has a product
            if data in blue:
                blue.remove(data)
                print('Blue product complete with ID: ', data)
            elif data in green:
                green.remove(data)
                print('Green product complete with ID: ', data)
            elif data in black:
                black.remove(data)
                print('Black product complete with ID: ', data)

            # Mixed production, two products
            # Check which product to make next
            next = randint(1,3)

            if next is 1:
                # Blue products
                blue.append(data)
                # print('Blue: ', blue)
                print('Assigning Blue product to ID: ', data)
                print(' ')
                command = b'1'
            elif next is 2:
                # Green products
                green.append(data)
                # print('Green: ', green)
                print('Assigning Green product to ID: ', data)
                print(' ')
                command = b'5'
            elif next is 3:
                # Black products
                black.append(data)
                # print('Black: ', black)
                print('Assigning Black product to ID: ', data)
                print(' ')
                command = b'3'
                # if next = 2:
                #     # Reset counter
                #     next = 0

            conn.send(command)
            # print('Sent: ', command)
            start = time.time()
            # next = next + 1
