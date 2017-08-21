#!/usr/bin/env python
# coding=utf-8



from socket import *
import sys
host = '10.10.2.191'
port = 7890
sock_server = (host,port)

def print_help():
    
    data = 'use this script as :python Client \'$6$9WbBd61T$bGOeNO09qbTDxsLLghNqoKPRlA.BzZQVOwvCs7CtfhX5y/diF1/pIQm.BsuhrzlP8BHcgC8YO8W.RH4L9dpYA1\' 1'
    print data

def main():
    if len(sys.argv)<3:
        print_help()
        return

    try:
        client_sock = socket(AF_INET, SOCK_STREAM)
        client_sock.connect(sock_server)
        data = sys.argv[1]
        data+=' '+sys.argv[2]
        print 'sending data:',data
        client_sock.sendall(data)
        print client_sock.recv(1024)
    except Exception as err:
        print (err)
if __name__ == '__main__':
    main()
