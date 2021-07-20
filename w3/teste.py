import scrapy

class Comenta_Spider(scrapy.Spider):
    name = 'w3'
    start_urls = ['https://www.w3schools.io/file/yaml-sample-example/']

    def parse(self, response):
        comentarios = response.xpath('//div//pre[@class="chroma"]/code[@class="language-Yaml"]/span').extract()

        for comenta in comentarios:
            yield {
                'comenta' : comenta
            }

    def parse_(self, response):
        pass
