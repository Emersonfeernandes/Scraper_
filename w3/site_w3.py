import scrapy

class Comenta_Spider(scrapy.Spider):
    name = 'w3'
    start_urls = ['https://www.w3schools.io/file/yaml-sample-example/']

    def parse(self, response):
        #comentarios = response.xpath('//div//code[@class="language-Yaml"]/span[@class="c"]').extract()
        comentarios = response.xpath('//div//pre[@class="chroma"]')

        for comenta in comentarios:
            yield {
                'c' : comenta.xpath('.//code[@class="language-Yaml"]/span[@class="c"]/text()').extract(),
                'nt' : comenta.xpath('.//code[@class="language-Yaml"]/span[@class="nt"]/text()').extract(),
                '1' : comenta.xpath('.//code[@class="language-Yaml"]/span[@class="1"]/text()').extract(),
                'm' : comenta.xpath('.//code[@class="language-Yaml"]/span[@class="m"]/text()').extract(),
                's2' : comenta.xpath('.//code[@class="language-Yaml"]/span[@class="s2"]/text()').extract(),
                's1' : comenta.xpath('.//code[@class="language-Yaml"]/span[@class="s1"]/text()').extract(),
                'sd' : comenta.xpath('.//code[@class="language-Yaml"]/span[@class="sd"]/text()').extract()
            }

    def parse_(self, response):
        pass
