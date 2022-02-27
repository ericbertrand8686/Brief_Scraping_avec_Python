import string
import scrapy
from scrapy import Request

class muzeoSpider(scrapy.Spider):

    name = "muzeo"
    
    start_urls = []
    
    with open("../5d952d11-046e-4a51-b29e-7d8b469435bf.txt") as f :
        for line in f:
            start_urls.append(line)


    def parse(self, response):
        # xp = "//div[@id='horiznav_nav']//li/a/@href"
        return (Request(url, callback=self.parse_manga_list_page) for url in response.xpath(xp).extract())



    def parse_muzeo_list_page(self, response):
        for tr_sel in response.css('div.js-categories-seasonal tr ~ tr'):
            yield {
                "title":  tr_sel.css('a[id] strong::text').extract_first().strip(),
                "synopsis": tr_sel.css("div.pt4::text").extract_first(),
                "type_": tr_sel.css('td:nth-child(3)::text').extract_first().strip(),
                "episodes": tr_sel.css('td:nth-child(4)::text').extract_first().strip(), 
                "rating": tr_sel.css('td:nth-child(5)::text').extract_first().strip()
            }

        next_urls = response.xpath("//div[@class='spaceit']//a/@href").extract()
        for next_url in next_urls:
            yield Request(response.urljoin(next_url), callback=self.parse_anime_list_page)

