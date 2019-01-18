#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:chengxiaotao time:2017/9/17

import socket


s = socket.socket()

host = socket.gethostbyname(socket.gethostname())
# print socket.gethostname()
# print host
port = 8888

s.connect((host,port))

while True:
    cmd = raw_input('请输入你的聊天内容:\n')

    if cmd == 'quit':
        break
    elif cmd == '':
        continue
    s.sendall(cmd)
    data = s.recv(1024)
    print data

s.close()