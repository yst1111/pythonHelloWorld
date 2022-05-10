from urllib import request
from urllib import parse


# 拼接URL地址 https://image.baidu.com/search/index?tn=baiduimage&ps={}
def get_url(word):
    url = 'https://image.baidu.com/search/index?tn=baiduimage&ps={}'
    # 此处使用urlencode()进行编码
    params = parse.urlencode({'wd': word})
    url = url.format(params)
    return url


# 发请求,保存本地文件
def request_url(url, filename):
    headers = { "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.16 Safari/537.36",}
    # 请求对象 + 响应对象 + 提取内容
    req = request.Request(url=url, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    # 保存文件至本地
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)


# 主程序入口
if __name__ == '__main__':
    word = input('请输入搜索内容:')
    url = get_url(word)
    filename = word + '.html'
    request_url(url, filename)
