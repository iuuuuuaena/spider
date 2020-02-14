from fake_useragent import UserAgent
#使用fake_useragent这个UA标识库中的数据
ua=UserAgent()
print(ua.chrome)
print(ua.firefox)