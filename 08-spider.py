#实例：从百度贴吧获取数据
from urllib.request import Request,urlopen
from urllib.parse import urlencode

#从服务器请求页面
def getHTML(url):
    headers={
        "User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 \
        (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    }
    request = Request(url, headers=headers)
    response = urlopen(request)
    result = response.read()
    return result
#把服务器请求来的页面保存到html文件里
def saveHTML(filename, html_bytes):
    with open(filename,"wb") as f:
        f.write(html_bytes)
#主函数文件，调用getHTML和saveHTML
def main():
    #content用于保存查询信息
    content = input("请输入要从贴吧查询的信息：")
    #num用于保存自定义的查询页数
    num = input("请输入最多查询的页数：")
    #使用格式化代码动态模拟网页查询url
    url = "http://tieba.baidu.com/f?&ie=utf-8&{}"
    #根据定义的查询页数循环请求网页并保存网页
    for pn in range(int(num)):
        args = {
            "pn":pn * 50,
            "kw":content
        }
    #定义文件名
    filename = "第"+str(pn)+"页.html"
    #进行url转码
    args = urlencode(args)
    print("正在下载"+filename)
    #请求网页
    html_bytes = getHTML(url.format(url))
    #查询网页
    saveHTML(filename ,html_bytes)
    


if __name__ == "__main__":
    main()