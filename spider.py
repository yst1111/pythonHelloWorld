import urllib.request
from urllib import request
from fake_useragent import UserAgent

# 爬取百度主页面
# response = urllib.request.urlopen('http://www.baidu.com/')
# html = response.read().decode('utf-8')
# print(response)

# # 重构爬虫UA信息 http://172.26.161.49/main
# # url = 'http://172.26.161.49/main'
# url = 'http://httpbin.org/get' #向测试网站发送请求
# headers = {
# 'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'}
# # 1、创建请求对象，包装ua信息
# req = request.Request(url=url,headers=headers)
# # 2、发送请求，获取响应对象
# res = request.urlopen(req)
# # 3、提取响应内容
# html = res.read().decode('utf-8')
# print(html)

# 第三方模块 随机生成UserAgent
#实例化一个对象
ua=UserAgent()
url = 'http://httpbin.org/get' #向测试网站发送请求
headers = {
'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0'}
req = request.Request(url=url,headers=headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')
print(html)
