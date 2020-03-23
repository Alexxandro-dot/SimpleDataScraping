# -*- coding: utf-8 -*-
import scrapy


class GlassesSpider(scrapy.Spider):
    name = 'glasses'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers/']

    def parse(self, response):
        
        items= response.xpath("//div[@class='col-sm-6 col-md-4 m-p-product']")
        for item in items:
            product_url=item.xpath(".//div/a/@href").get()
            product_image= item.xpath(".//div/a/img[2]/@src").get()
            product_name= item.xpath(".//div[2]/p/a/text()").get()
            product_price= item.xpath(".//div[2]/p/a/text()").get()
                 
            yield{                
                'product_name':product_name,
                'product_price':product_price,
                'product_url':product_url,
                'product_image':product_image,
                               
                }

            next_page= response.xpath("//li[@class='page-item']/a/@href").get()
            if next_page:
                yield response.follow (url=next_page)