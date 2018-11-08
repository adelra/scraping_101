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



fp = open('output_wikipedia.txt', 'w')
# fp.write("link" +"\t"+ "title"+"\t"+"content")

class IrnaSpider(CrawlSpider):
    name = 'general'
    allowed_domains = ['en.wikipedia.org']
    start_urls = [
'https://en.wikipedia.org/wiki/Main_Page'
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
        item["title"] =re.sub(r"<[^>]*>","","".join(response.css("#firstHeading").extract()))

        #re.sub(r"[a-zA-Z<>\\\"=/:]*","","".join(response.css(".JobTitle , .JobDetailList").extract()).encode('utf-8'))
        item["content"] = re.sub(r"<[^>]*>","","".join(response.css("#content").extract()))
        if item["link"] is None:
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
