'''
爬取图片
'''
# -*- coding:utf-8 -*-
# import urllib
import  urllib.request
import re

def download_page(url):
headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64;'
                        ' Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729;'
                        ' Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)'}
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
data = response.read()
return data

def get_image(html):
regx ='src="(.+?\.jpg)"'
imgre = re.compile(regx)
imglist = re.findall(imgre,html.decode('utf-8'))     # py3的urlopen返回的不是string是bytes。html用decode(‘utf-8’)进行解码，由bytes变成string。

num =1
for imgurl in imglist:
    image = download_page(imgurl)         #重新解析每个图片的链接，返回bytes类型
    with open('%s.jpg' % num,'wb') as fp:        #以二进制+写文件 形式打开一个.jpg文件
        fp.write(image)                            #写文件
        print('正在下载第%s张图片' % num)
        num +=1
return

url = 'http://tieba.baidu.com/p/5577092638'
html = download_page(url)
get_image(html)




###################第二种方式######################
# -*- coding:utf-8 -*-
import urllib
import  urllib.request
import re

def getHtml(url):
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    html = response.read()
    return html

def getImg(html):
    reg = 'src="(.+?\.jpg)"'        #正则表达式
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html.decode('utf-8'))
    x = 1
    for imgurl in imglist  :
        urllib.request.urlretrieve(imgurl,'%s.jpg' % x)    # 设置了要下载的图片资源路径和要命名的名字
        print('正在下载第%s张图片' % x)
        x+=1
        if x>6:                     #设置爬取图片的张数
            break
    return None

html = getHtml("http://tieba.baidu.com/p/5577092638")
getImg(html)
