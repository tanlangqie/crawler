# -*- coding: utf-8 -*-
import scrapy


class ShspiderSpider(scrapy.Spider):
    name = 'shSpider'
    allowed_domains = ['hshfy.sh.cn']
    start_urls = ['http://hshfy.sh.cn/']

    def parse(self, response):
        pass
