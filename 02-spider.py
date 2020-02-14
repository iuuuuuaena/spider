#引入urlopen发送请求的函数
from urllib.request import urlopen
#引入Request函数
from urllib.request import Request

url="http://www.baidu.com"
# url 作为Request()方法的参数，
# 构造并返回一个Request对象
request=Request(url)
#Request对象作为urlopen()方法的参数，
#发送给服务器并接收响应
response=urlopen(request)
# read()方法读取文件全部内容，返回字符串
result=response.read()
# Python decode() 方法以 encoding 指定的编码格式解码字符串。
# 默认编码为utf-8编码。
print(result.decode())
#输出请求的反应码
print("反应码为：",response.getcode())
#输出真实请求的url
print("url为：",response.geturl())
#输出响应头的具体信息
print("http相应头为：",response.info())


