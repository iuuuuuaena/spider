# 代理IP的使用
from urllib.request import ProxyHandler
from urllib.request import build_opener
from urllib.request import Request
from random import choice
import ssl

ssl.create_default_context = ssl._create_unverified_context

url = "http://www.baidu.com"

UA=[
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"]
headers = {
    "User-agent":choice(UA)
}

request = Request(url,headers=headers)

#1.使用ProxyHandler，传入构建一个Handler
#这里的ProxyHandler里面传入一个字典，协议：ip，这里可以放入我们从网上找到的代理IP
proxy_handler = ProxyHandler({
    'http': '127.0.0.1:8080'
})
#2.使用上面创建的Handler构建一个opener
opener = build_opener()
#3.用opener去发送一个请求
response = opener.open(request)
print(response.read().decode())