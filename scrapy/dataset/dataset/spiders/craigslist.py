# -*- coding: utf-8 -*-
from __future__ import print_function
import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import re

class IrnaItem(scrapy.Item):
    # define the fields for your item here like:
    link = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()



fp = open('output_craigslist.txt', 'w')
# fp.write("link" +"\t"+ "title"+"\t"+"content")

class IrnaSpider(CrawlSpider):
    name = 'craigslist'
    allowed_domains = ['craigslist.org']
    start_urls = [
'https://tehran.craigslist.org/ctd/d/dammam-lexus-lx/6737131720.html'
    ]
    rules = [
        Rule(LinkExtractor(),callback='parse_news', follow=True),
        ]
    # def parse(self, response):
    #     sel = response
    #     links = sel.xpath('//a/@href').extract()
    #     for link in links:
    #         absolute_url = self.start_urls[0] + link
    #         yield scrapy.Request(absolute_url, callback=self.parse_news)

    def parse_news(self, response):
        item = IrnaItem()
        item["link"] = response.url
        item["title"] =re.sub(r"<[^>]*>","","".join(response.css("#titletextonly").extract()))

        #re.sub(r"[a-zA-Z<>\\\"=/:]*","","".join(response.css(".JobTitle , .JobDetailList").extract()).encode('utf-8'))
        item["content"] = re.sub(r"<[^>]*>","","".join(response.css("#postingbody").extract()))
        if item["content"] is None:
            return None
        if item["title"] is None:
            return None
        else:
            fp.write("\n"+item["link"] +"\n"+item["title"]+"\n"+item["content"]+"\n"+"="*64)
            return item
        # if item["attr"] is not None:
        #     return item
        # else:
        #     yield scrapy.Request(item["link"], callback=self.parse)

        # def get_links(self, link):
        #     yield scrapy.Request(link, callback=self.parse)

        # def parse_inner_pages(self, link):
        #     yield scrapy.Request(url=link, callback=self.parse)
