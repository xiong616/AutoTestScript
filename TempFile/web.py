# -*- coding: utf-8 -*- 
'''
Created on 2016年8月18日

@author: xiong
'''

#!/usr/bin/env python
#coding:utf-8
 
import socket
 
def handle_request(client):
    buf = client.recv(1024)
    client.send("HTTP/1.1 200 OK\r\n\r\n")
    client.send("Hello, Seven")
 
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('192.168.0.104',80))
    sock.listen(5)
 
    while True:
        connection, address = sock.accept()
        handle_request(connection)
        connection.close()
 
if __name__ == '__main__':
    main()