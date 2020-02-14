#导入urllib下的urlopen
from urllib.request import urlopen
#url
url = "http://www.baidu.com"
#向服务器发送请求
response = urlopen(url)
#读取返回的信息
result = response.read()
#输出返回的html
print(result.decode())
#输出请求的反应码
print("反应码为：",response.getcode())
#输出真实请求的url
print("url为：",response.geturl())
#输出响应头的具体信息
print("http相应头为：",response.info())
