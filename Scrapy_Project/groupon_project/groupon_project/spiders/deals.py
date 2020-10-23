import scrapy


class DealsSpider(scrapy.Spider):
    name = 'deals'
    allowed_domains = ['www.groupon.com']
    start_urls = ['http://www.groupon.com/landing/deal-of-the-day']

    def parse(self, response):
        for product in response.xpath("//div[@class='grpn-dc-caption']"):
            yield{
                "title" : product.xpath(".//div[@class='grpn-dc-title']/text()").get(),
                "price" : product.xpath(".//span[@class='wh-dc-price-discount c-txt-price']/text()").get(),
                "products_sold" : product.xpath(".//div[@class='grpn-rating']/text()").get()
            }
