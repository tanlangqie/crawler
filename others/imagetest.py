# -*- coding:utf-8 -*-
# import urllib
import  urllib.request
import re
'''
fun: 爬取网络中的图片
time: 2017
author: tang
'''
def download_page(url):
    headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)'}
    request = urllib.request.Request(url,headers=headers)

    try:
        response = urllib.request.urlopen(request)        #如果response异常

    except:
        return None
    data = response.read()

    print(data)
    return data

def get_image(html):
    regx ='src="(.+?\.jpg)"'
    # regx = r'src="http://(.*?)"\.jpg'

    imgre = re.compile(regx)
    imglist = re.findall(imgre,html.decode('utf-8'))
    num =110
    for imgurl in imglist:
        image = download_page(imgurl)
        if(image==None) :
            continue
        with open('%s.jpg' % num,'wb') as fp:
            fp.write(image)
            num +=1
            print('正在下载第%s张图片'%num)
    return

url = 'http://pic.yxdown.com/list/0_0_1.html'
html = download_page(url)
get_image(html)
print('000')