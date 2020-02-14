from random import choice
from urllib.request import urlopen
from urllib.request import Request
#四种不同的UA标识
UA=[
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"]
#自定义随机请求头
headers={
    "User-agent":choice(UA)
}
print(headers)
#url
url='http://www.baidu.com'
request=Request(url,headers=headers)
#发送请求
response=urlopen(request)
result=response.read()
print("url:",response.geturl())
print("返回的为：",result.decode())