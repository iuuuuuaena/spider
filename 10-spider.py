from urllib.request import urlopen,Request
from urllib.parse import urlencode
from random import choice
import ssl

#全局取消证书验证
ssl._create_default_https_context = ssl._create_unverified_context

# url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"
# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20
# https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=80&limit=20
# 通过比较，我们发现，用Ajax实时请求的电影数据之间的区别为后面的 start
# 我们想要爬取所有的电影信息，只需要模拟发送start不一样的get请求即可
#四种不同的UA标识
base_url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start={}&limit=20"
UA=[
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"]
# 循环
i = 0 
while True:
    #自定义随机请求头
    headers={
    "User-agent":choice(UA)
    }
    #伪造翻页的url
    url = base_url.format(i * 20)
 
    request = Request(url,headers=headers)

    # context = ssl._create_unverified_context()
    response = urlopen(request)

    info = response.read().decode()

    print(info)
    # 如果请求返回的是空或者None，则标识下面已经没有电影了，就结束
    if info == "" or info == None:
        break
    i += 1