#实例：从百度贴吧获取数据
from urllib.parse import urlencode
from urllib.request import Request,urlopen

#获取页面html
def getHTML(url):
    headers={
        "User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    }
    request=Request(url,headers=headers)
    response=urlopen(request)
    result=response.read()
    return result

#保存页面信息
def saveHTML(filename,html_bytes):
    with open(filename,"wb") as f:
        f.write(html_bytes)


def main():

    content =input("请输入要查询的内容：")
    num = input("请输入要下载的页数：")
    url="http://tieba.baidu.com/f?&ie=utf-8&{}"
    for pn in range(int(num)):
        args={
            "pn":pn * 50,
            "kw":content
        }
        filename="第"+str(pn+1)+"页.html"
        args=urlencode(args)
        print("正在下载"+filename)
        html_bytes = getHTML(url.format(args))
        saveHTML(filename,html_bytes)
    

if __name__ == "__main__":
    main()