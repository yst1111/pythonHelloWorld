import requests

url = 'http://www.baidu.com/s'

headers = {
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.16 Safari/537.36",
}

params = {
    'kw':'周冬雨'
}

resp = requests.get(url,headers=headers,params=params).content.decode()
print(resp)