# -*- coding: utf-8 -*-
"""
 @Time: 2019/6/5 15:32
"""

import time
import os
import sys

import requests
from urllib.parse import quote
import re
import json
import base64

# url = "http://www.baidu.com/"

# lua = """
# function main(splash, args)
#     local treat = require("treat")
#     local response = splash:http_get("http://httpbin.org/get")
#     return treat.as_string(response.body)
# end
# """

# lua = """
# function main(splash, args)
#     local treat = require("treat")
#     local json = require("json")
#     local response = splash:http_get{"http://www.gsxt.gov.cn", headers={["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}}
#     return {html= treat.as_string(response.body),
#             url = response.url,
#             status = response.status,
#             cookies = splash:get_cookies()}
# end
# """

# lua = """
# function main(splash, args)
#     local treat = require("treat")
#     local json = require("json")
#     splash:add_cookie{"__jsluid", "0f782610b1db0088a6bb21ed15735fe5", '/', domain = "www.gsxt.gov.cn"}
#     local response = splash:http_get{"http://www.gsxt.gov.cn", headers={["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}}
#     return {html= treat.as_string(response.body),
#             url = response.url,
#             status = response.status,
#             cookies = splash:get_cookies()}
# end
# """

lua = """
function main(splash, args)
    local treat = require("treat")
    local json = require("json")
    local response = splash:http_get{"https://www.taobao.com", headers={["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}}
    return {html= treat.as_string(response.body),
            url = response.url,
            status = response.status,
            png = splash:png(),
            cookies = splash:get_cookies()}
end
"""

url = "http://192.168.5.32:8050/execute?lua_source=" + quote(lua)
response = requests.get(url)
data = json.loads(response.text)
print(data["html"])
# print(data["png"])
with open('taobao.png', 'wb') as f:
    f.write(base64.b64decode(data["png"]))


# ip =
