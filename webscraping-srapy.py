import scrapy

url = "http://books.toscrape.com/"

class BookSpider(scrapy.Spider):
    name = "bookspider"
    start_urls = [url]

    def parse(self, response):
        # <article class = "product_pod"....
        for article in response.css("article.product_pod"):
            yield {
                # class = price_color
                "price": article.css(".price_color::text").extract_first(), # or use .get() instead of extract_first, but getall() will return a list
                # <h3 ...> <a title = "info i want" ... > </h3>
                "title": article.css("h3 > a::attr(title)").extract_first()
            }
        import pdb; pdb.set_trace() # using command to run this file in pdb mode: scrapy runspider -o books.csv webscraping-srapy.py --pdb

        #next = response.css(".next > a::attr(href)").extract_first()
        next = response.css(".next > a")[0] # selector可以直接传入， 而且不需要写attr(href) 因为对于a element默认解析attr的值
        # 可以直接写
        if next:
            yield response.follow(next, self.parse)

