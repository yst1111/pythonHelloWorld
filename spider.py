import urllib.request
from urllib import request
from fake_useragent import UserAgent

# 爬取百度主页面
# response = urllib.request.urlopen('http://www.baidu.com/')
# html = response.read().decode('utf-8')
# print(response)

# # 重构爬虫UA信息
# # url = 'http://172.26.161.49/main'
# url = 'http://httpbin.org/get'
# headers = {
# 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'}
# req = request.Request(url=url,headers=headers)
# res = request.urlopen(req)
# html = res.read().decode('utf-8')
# print(html)

# 第三方模块 随机生成UserAgent
ua = UserAgent()
url = 'https://httpbin.org/get'  # 向测试网站发送请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36'}
req = request.Request(url=url, headers=headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')
print(html)
