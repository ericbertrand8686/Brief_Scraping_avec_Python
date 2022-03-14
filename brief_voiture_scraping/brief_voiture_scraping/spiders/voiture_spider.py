import string
import scrapy
import re

class voitureSpider(scrapy.Spider):

    custom_settings = {
    'ROBOTSTXT_OBEY': False
    }
    
    name = "voiture"
    
    def start_requests(self):

        res = []
        with open("liste_url.txt") as f :
             urls = [url.strip()[1:-1] for url in f.readlines()]
        
        urls=urls[0:10]

        for url in urls:
            res.append(scrapy.Request(url=url, callback=self.parse))

        return res


    def parse(self, response):
        yield {
                "Version":  response.xpath('//*[@id="mes-ht"]/ul/li[1]/span/text()').extract_first(),
                "Prix": response.xpath('//*[@id="mes-ht"]/ul/li[2]/span/text()').extract_first(),
                "Année":  response.xpath( '//*[@id="mes-ht"]/ul/li[3]/span/text()').extract_first(),
                "Kilométrage": response.xpath( '//*[@id="mes-ht"]/ul/li[4]/span/text()').extract_first(),
                "Energie": response.xpath( '//*[@id="mes-ht"]/ul/li[5]/span/text()').extract_first(),
                "Emissions": response.xpath( '//*[@id="mes-ht"]/ul/li[6]/span/text()').extract_first(),
                "Consommation": response.xpath( '//*[@id="mes-ht"]/ul/li[7]/span/text()').extract_first(),
                "Transmission": response.xpath( '//div[@id="papier_peint_mes_img"]').extract_first(),
                "Portes":  response.xpath( '//*[@id="mes-ht"]/ul/li[9]/span/text()').extract_first()
        }
        return
