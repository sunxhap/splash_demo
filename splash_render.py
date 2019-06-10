# -*- coding: utf-8 -*-
"""
 @Time: 2019/6/5 15:54
"""

import time
import os
import sys


# import requests
# url = 'http://192.168.5.32:8050/render.html?url=https://www.taobao.com&wait=5'
# response = requests.get(url)
# print(response.text)

import requests
url = 'http://192.168.5.32:8050/render.png?url=https://www.toutiao.com/&width=1000&height=700&wait=5'
response = requests.get(url)
with open('toutiao.png', 'wb') as f:
    f.write(response.content)
