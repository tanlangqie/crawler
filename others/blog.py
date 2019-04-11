'''
fun: 给博客刷浏览量（浏览某一页面中出现的所有链接）
time: 2017
author: tang
'''
# -*- coding:utf-8 -*-
import re
import urllib
import urllib.request     #在python2中为urllib2.Request
from lxml.html import parse
from urllib.request import urlopen       #在python2中为urllib2.urlopen

def get_htmls(url):
    '''
    #得到一个页面内的所有网页链接
    '''

    # 用lxml解析得到数据流
    parsed = parse(urlopen(url))
    doc = parsed.getroot()

    list_link =[]
    list_html = []
    #所有网页的链接的标签都是a, 用文档根节点的findall方法以及一个xpath找出网页链接
    links = doc.findall('.//a')
    for link in links:
        m = str(link.get('href'))      #得到网页的链接

        if len(m)>4 and m[0:4]=='http':
            list_link.append(m)
    #print(list_link)
    return list_link

def get_content(list_link):
    agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0"
    header = {"user_agent": agent}

    i = 0
    #对每一个链接读取网页的内容
    for url in list_link :
        i = i +1     #计数
        if i<3:
            continue
        if i >= 15:
            break
        request = urllib.request.Request(url, headers=header)
        try:
            response = urllib.request.urlopen(request)
            data = response.read()

        except:
            print('Finding an Error!')

        regx = '<h6 class="title-article">(.*?)</h6>'
        pattern = re.compile(regx,re.S)
        title = re.findall(pattern, data.decode('utf-8'))

        #write_to_file(title)

    return


def write_to_file(title):
    f = open('./blog.txt','a+',encoding='utf-8')   #打开一个文件用于追加内容
    f.write(title)
    f.write('\n')
    f.close()

#main
#if __name__ == "__main__":
    #list_link = get_htmls('https://blog.csdn.net/tanlangqie/article/list/2')
    #print(list_link)    #输出路径
for i in range(200):
    list_link = get_htmls('https://blog.csdn.net/tanlangqie')  # https://blog.csdn.net/tanlangqie/article/list/2
    get_content(list_link)
    print('第%d遍'%(i))