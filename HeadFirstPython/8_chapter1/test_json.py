# coding=utf-8

import json

names = ['John', ['Johnny', 'Jack'], 'Michael', ['Mike', 'Mikey', 'Mick']]

# 将Python多重list转换成一个JSON多重列表
to_transfer = json.dump(names, 'write')


# 将json格式转换成list
from_transfer = json.load(to_transfer)