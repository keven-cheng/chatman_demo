#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:chengxiaotao time:2017/9/17

import socket
import urllib
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def get_computer(info):
    # info = 'python'
    key = '56c44f6ac95541c6a968bebaa913855d' # 申请的图灵机器人的API http://www.tuling123.com/
    api = 'http://www.tuling123.com/openapi/api?key='+key+'&info='+info

    response = urllib.urlopen(api).read()
    dict_json = json.loads(response)
    # print type(dict_json)
    return u'机器人kevin：'.encode('utf-8')+dict_json['text']


host = socket.gethostbyname(socket.gethostname())
print host
port = 8888

s = socket.socket()

s.bind((host,port))

s.listen(1)

while True:
    clnt, addr = s.accept()
    print 'client address:',addr

    while True:
        data = clnt.recv(1024)

        if not data:
            sys.exit()
        print 'going to:',data
        result = get_computer(data)
        if len(result) == 0:
            result = 'EXD'
        clnt.sendall(result)

clnt.close()