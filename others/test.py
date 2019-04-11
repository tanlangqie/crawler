# -*- coding:utf-8 -*-
import urllib
import  urllib.request
import re
'''
两种爬取图片方法的其中一种

'''
def getHtml(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    html = response.read()
    return html

def getImg(html):
    reg = 'src="(.+\.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html.decode('utf-8'))

    x = 1
    for imgurl in imglist  :
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)    # 设置了要下载的图片资源路径和要命名的名字
        print('正在下载第%s张图片' % x)
        x+=1
        if x>60:                     #设置爬取图片的张数
            break
    return None

html = getHtml("http://tieba.baidu.com/p/5577092638")
getImg(html)
