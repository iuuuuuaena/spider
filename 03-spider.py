from urllib.request import urlopen
from urllib.request import Request
#1.url
url='http://www.baidu.com'
#2.请求头信息，使用chrome的user-agent
headers={
    "User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
#3.使用chrome的请求头信息伪装请求
request=Request(url,headers=headers)
#注意这里首字母大写，U是大写的，a不是
print(request.get_header("User-agent"))
#4.向服务器发送请求
response=urlopen(request)
#5.返回信息
result=response.read()
# print("返回的信息为：",result.decode())
print("-----------------------")
print("url为:",response.geturl())

