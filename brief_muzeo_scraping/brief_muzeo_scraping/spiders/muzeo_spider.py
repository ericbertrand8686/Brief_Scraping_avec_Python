import string
import scrapy
import re

class muzeoSpider(scrapy.Spider):

    name = "muzeo"
    
    def start_requests(self):

        res = []
        
        with open("5d952d11-046e-4a51-b29e-7d8b469435bf.txt") as f :
             urls = [url.strip()[1:-1] for url in f.readlines()]
             # le [1:-1] permet d'éliminer les quotes " de l'url qui perturbent la méthode GET
             
        
        # urls=urls[0:10] # inactivé, utile pour certains tests à petite échelle
        
        # on invoque un parse pour chaque url de la liste
        for url in urls:
            res.append(scrapy.Request(url=url, callback=self.parse))

        return res


    def parse(self, response):
        
        # une regex pour l'url de l'image
        reurl= r"https?:\/\/.+[\?\\]"
        
        # préparation du résultat du parse
        yield {
                "Titre":  response.xpath('//title/text()').extract_first(),
                "ID produit": response.xpath( "//span[@id='ref_product']/text()").extract_first(),
                "Prix":  response.xpath( "//div[@id='edit-price']/div[2]").extract_first(),
                "Delai de fabrication": response.xpath( "//div[@id='delai_fabrication']/strong").extract_first(),
                "Url de l'image": re.findall( reurl , response.xpath( "//div[@id='papier_peint_mes_img']").extract_first() )[0]
        }
        return
