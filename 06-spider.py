#第六个练习呢，我们来看下get请求的问题
''' 1.我们可以在百度搜索页面，随便搜索一个东西，比如我这里搜索jxd这三个字母
    2.然后我们看下url,就是下面这个
        https://www.baidu.com/s?wd=jxd&rsv_spt=1&rsv_iqid=0xd39d1685000db5fa&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=4&rsv_sug1=4&rsv_sug7=101&rsv_sug2=0&inputT=1951&rsv_sug4=2529
        我们把其他的东西都去掉，剩下
        https://www.baidu.com/s?wd=jxd
        这个东西我们直接复制粘贴到搜索框，看一下运行是什么结果
        我们可以看到，还是跟直接搜索jxd一样，百度呢，也把jxd的搜索结果直接显示出来了

    3.我们想要模拟百度发送搜索的链接，我们就需要像这样把我们要搜索的值放到wd=？？？这后面，
        但是我们会发现，直接用汉子搜索，会搜不到，由于编码方式不同，我们要把utf-8转化为URL编码
        ，所以我们需要使用python给我们提供的转码方式，把我们要搜索的东西，用quote（)或者 urlencode  
        进行URL编码，然后就可以直接搜索了。

'''
from random import  choice
#引入转码的函数
from urllib.parse import quote 
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode

#相当于输出了”你好啊“的转码之后的
print(quote("你好啊！"))
'''这就是转码之后的格式
    %E4%BD%A0%E5%A5%BD%E5%95%8A%EF%BC%81
'''
args={
    "wd":"你好啊！",
    "ie":"UTF-8"
}
url1="http://www.baidu.com/s?wd={}".format(quote("你好啊！"))

url2="http://www.baidu.com/s?{}".format(urlencode(args))
UA=[
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"]
#自定义随机请求头
headers={
    "User-Agent":choice(UA)
}
request1=Request(url1,headers=headers)
request2=Request(url2,headers=headers)
# response1=urlopen(request1)
response2=urlopen(request2)

# result1=response1.read()
result2=response2.read()

print(result2.decode())
