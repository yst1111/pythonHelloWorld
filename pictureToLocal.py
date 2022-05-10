import requests

#图片写入本地
url = 'https://img0.baidu.com/it/u=2205190407,2717370642&fm=253&fmt=auto&app=138&f=PNG?w=500&h=322'
#简单定义浏览器ua信息
headers = {'User-Agent':'Mozilla/4.0'}
#读取图片需要使用content属性
html = requests.get(url=url,headers=headers).content
#以二进制的方式下载图片
with open(r'D:/files/java.jpg','wb') as f:
    f.write(html)