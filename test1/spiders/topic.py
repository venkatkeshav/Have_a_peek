import scrapy


class TopicSpider(scrapy.Spider):
    name = 'topic'
    allowed_domains = ['learnawesome.org']
    start_urls = ['https://learnawesome.org/topics/']

    def parse(self, response):
        for link in response.css("div.inline-block a::attr(href)"):
            print(link)
            yield response.follow(link.get(), callback = self.parse_categories)

    def parse_categories(self , response):
        products = response.css("div.px-4 a::attr(href)").getall()
        for product in products:
            product1 = response.urljoin(product)
            yield response.follow(product1 , callback = self.parse_link)
        
    def parse_link(self, response):
        links = response.css("article.px-4 a::attr(href)").getall()
        for i in links:
            if i[8:11]!="lea" and i[0:3]=="htt":
                i = response.urljoin(i)
                for j in (response.css("div.mb-4 a::text").getall())[1:]:

                    yield  {"link":i,
                "name":response.css("article.px-4 h1::text").getall(),
                "topic" :j}
                 #"item_topic" : response.css("div.mb-4 a::text").getall()
                
