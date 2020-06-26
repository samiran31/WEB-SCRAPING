# -*- coding: utf-8 -*-
import scrapy


class GlassSpiderSpider(scrapy.Spider):
    name = 'glass_spider'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        for product in response.xpath("//div[@class='product-img-outer' or @class='col-6 col-lg-6']"):
            url=product.xpath(".//div/a/@href").get()
            name=product.xpath(".//div/a/@title").get()
            price=product.xpath(".//div/div/span/text()").get()
            link=product.xpath(".//a/img[1]/@src").get()

            
            yield{
                'product_url':url,
                'product_name':name,
                'product price':price,
                'product_image_link':link
            }
        next_page = response.xpath("//ul[@class='pagination']/li[position() = last()]/a/@href").get()
        print(next_page) 
        if next_page:
            yield scrapy.Request(url=next_page, callback=self.parse)
