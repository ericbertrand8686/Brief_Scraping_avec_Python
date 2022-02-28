import string
import scrapy
import re

class muzeoSpider(scrapy.Spider):

    name = "muzeo"
    
    def start_requests(self):

        res = []
        with open("5d952d11-046e-4a51-b29e-7d8b469435bf.txt") as f :
             urls = [url.strip()[1:-1] for url in f.readlines()]
        
        urls=urls[0:10]

        for url in urls:
            res.append(scrapy.Request(url=url, callback=self.parse))

        return res


    def parse(self, response):
        reurl= r"https?:\/\/.+[\?\\]"

        yield {
                "Titre":  response.xpath('//title/text()').extract_first(),
                "ID produit": response.xpath( "//span[@id='ref_product']/text()").extract_first(),
                "Prix":  response.xpath( "//div[@id='edit-price']/div[2]").extract_first(),
                "Delai de fabrication": response.xpath( "//div[@id='delai_fabrication']/strong").extract_first(),
                "Url de l'image": re.findall( reurl , response.xpath( "//div[@id='papier_peint_mes_img']").extract_first() )[0]
        }
        return
