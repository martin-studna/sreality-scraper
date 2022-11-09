import scrapy
from flat_post_repository import FlatPostRepository

class SrealitySpider(scrapy.Spider):
    name = 'srealityspider'
    allowed_domains = ['sreality.cz']
    
    custom_settings = {
        "DOWNLOAD_HANDLERS": {
            "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
            "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
        },
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor",
    }
    
    def __init__(self, repository: FlatPostRepository, name=None, **kwargs):
        super().__init__(name, **kwargs)
        self.repository = repository
        self.counter = 0
    
    def start_requests(self):
        for i in range(1, 30):
            if self.counter == 500:
                return
            yield scrapy.Request(f"https://www.sreality.cz/en/search/for-sale/apartments?page={i}",
                                meta={"playwright": True})

    def parse(self, response):
        
        for item in response.css(".property.ng-scope"):
            if self.counter == 500:
                return
            imageSrc = item.xpath("preact/div/div/a/img/@src").get()
            title = item.xpath("div/div/span/h2/a/span/text()").get()
            locality = item.xpath('div/div/span/span[@class="locality ng-binding"]/text()').get()
            title += " " + locality 
            print(imageSrc)
            print(title)
            self.repository.add_new_post(title, imageSrc)
            self.counter += 1
            
            
