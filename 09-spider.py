from urllib.request import Request,urlopen
from urllib.parse import urlencode

#url
url="http://www.sxt.cn/index/login/login.html"
#POST请求的数据
from_data={
    "user":"17703181473",
    "password":"123456"
    }
#请求头
headers={
    "User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
}
#转码
from_data = urlencode(from_data)
#POST请求头
request = Request(url,data=from_data.encode(),headers=headers)
#发送请求
response = urlopen(request)
#打印请求
print(response.read().decode())
