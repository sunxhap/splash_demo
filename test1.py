# -*- coding: utf-8 -*-
"""
 @Time: 2019/6/5 13:34
"""

import time
import os
import sys

"""
function main(splash, args)
  local example_urls = {"www.baidu.com", "www.taobao.com", "www.zhihu.com"}
  local urls = args.urls or example_urls
  local results = {}
  for index, url in ipairs(urls) do  --迭代函数 ipairs
    local ok, reason = splash:go("http://" .. url)  -- 字符串拼接使用的是..操作符
    if ok then  -- 做了加载时的异常检测。go()方法会返回加载页面的结果状态，如果页面出现4xx或5xx状态码，ok变量就为空，就不会返回加载后的图片
      splash:wait(2)
      results[url] = splash:png()
    end
  end
  return results  -- 返回是3个站点的截图
end
"""

"""
function main(splash, args)
  assert(splash:go(args.url))
  splash.scroll_position = {x=100,y=400}
  return {
    png = splash:png(),
  }
end

"""


"""
function main(splash, args)
  local ok, reason = splash:go{"http://httpbin.org/post", http_method="POST", body="name=Hubo"}
  if ok then
        return splash:html()
  end
end
"""


"""
function main(splash, args)
  local ok, reason = splash:go{"https://www.baidu.com/", http_method="GET", headers={["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}}
  if ok then
        splash:wait(2)
        return {html = splash:html(),
                png = splash:png(),
                har = splash:har()}
  end
end
"""


"""
function main(splash, args)
  local ok, reason = splash:go{"https://www.taobao.com/", http_method="GET", headers={["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}}
  if ok then
        splash:wait(2)
        return {html = splash:html(),
                png = splash:png(),
                har = splash:har()}
  end
end
"""
# http://www.useragentstring.com/

"""
function main(splash, args)
  local ok, reason = splash:go{"http://www.useragentstring.com/", http_method="GET"}
  if ok then
        return splash:html()
  end
end
"""


# 设置 headers body
# body = json.encode({name="test"})
"""
function main(splash, args)
  local ok, reason = splash:go{"http://www.useragentstring.com/", http_method="GET", headers={["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36" }}
  if ok then
        return splash:html()
  end
end
"""

"""
function main(splash, args)
  local ok, reason = splash:go{"http://www.gsxt.gov.cn/index.html", http_method="GET", headers={["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", ["host"]="www.gsxt.gov.cn" }}
  if ok then
        return splash:html()
  end
end
"""

"""
function main(splash, args)
  local ok, reason = splash:go{"http://www.useragentstring.com/", http_method="GET", headers={["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", ["host"]="www.gsxt.gov.cn" }}
  if ok then
        return {html= splash:html(),
                url = }
  end
end
"""

# local ok, reason = splash:go{"http://www.useragentstring.com/", http_method="GET", headers={["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", ["host"]="www.gsxt.gov.cn" }}
# http://www.gsxt.gov.cn

"""
function main(splash, args)
    local treat = require("treat")
    local json = require("json")
    local response = splash:http_get{"http://www.gsxt.gov.cn", headers={["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}}
    return {html= treat.as_string(response.body),
            url = response.url,
            status = response.status,
            png = splash:png(),
            cookies = splash:get_cookies()}
end
"""

"""
function main(splash, args)
    local treat = require("treat")
    local json = require("json")
    local response = splash:http_get{"http://www.gsxt.gov.cn", headers={["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}}
    return {html= treat.as_string(response.body),
            url = response.url,
            status = response.status,
            cookies = splash:get_cookies()}
end
"""

"""
    splash:add_cookie{"__jsluid", "10e0a22253085e3efa0123dc88dab7c4", '/', domain = "www.gsxt.gov.cn"}
    splash:add_cookie{"__jsl_clearance", "1559717029.238|0|LshpZx5cclbYxo86oCxQguzdYzo%3D", '/', domain = "www.gsxt.gov.cn"}
"""


"""
function main(splash, args)
    local treat = require("treat")
    local json = require("json")
    local response = splash:http_get{"http://www.gsxt.gov.cn/index.html", headers={["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}}
    splash:wait(2)
    return {html= treat.as_string(response.body),
            url = response.url,
            status = response.status,
            png = splash:png(),
            cookies = splash:get_cookies()}
end
"""

"""
function main(splash, args)
    local treat = require("treat")
    local json = require("json")

    local response = splash:http_get{"https://www.jianshu.com/search?q=%E5%8C%BA%E5%9D%97%E9%93%BE&utm_source=desktop&utm_medium=search-recent", headers={["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}}
    splash:wait(2)
    return {html= treat.as_string(response.body),
            url = response.url,
            status = response.status,
            png = splash:png(),
            cookies = splash:get_cookies()}
end
"""



"""
function main(splash, args)
  local ok, reason = splash:go{"http://www.gsxt.gov.cn/index.html", http_method="GET", headers={["User-Agent"]="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"}}
  if ok then
        splash:wait(5)
        return {html = splash:html(),
                png = splash:png(),
                har = splash:har()}
  end
end
"""