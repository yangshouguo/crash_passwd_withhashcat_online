#!/usr/bin/env python
# coding=utf-8



from socket import *
import random
host = 'localhost'
port = 7890
sock_server = (host,port)

def main():
    try:
        client_sock = socket(AF_INET, SOCK_STREAM)
        client_sock.connect(sock_server)
        data = random.sample('abcdefghijklmnz',8)
        data = ''.join(data)
        data += ' 2'
        print 'sending data:',data
        client_sock.sendall(data)
        print client_sock.recv(1024)
    except Exception as err:
        print (err)
if __name__ == '__main__':
    main()
