import scrapy
from bs4 import BeautifulSoup
import requests
from ..items import ZlibBookItem
# from slugify import  slugify
# from urllib.parse import urlparse
# from urllib import parse

class ZlibSpiterSpider(scrapy.Spider):
    name = 'zlib_spiter'
    page_number = 2
    start_urls = [
        'https://eg1lib.org/s/python?page=1'
    ]

    def parse(self, response):

        items = ZlibBookItem()
        book_link_download =[]
        all_links = response.css("div.exactMatch")
        for link in all_links:
            book_title = link.css("h3 a::text").extract()
            book_author = link.css(".color1:nth-child(1)::text").extract()
            year = link.css(".property_year .property_value").css("::text").extract()
            language = link.css(".text-capitalize::text").extract()
            file_type_size = link.css(".property__file .property_value").css("::text").extract()
            rate_interest = link.css(".book-rating-interest-score::text").extract()
            rate_quality = link.css(".book-rating-quality-score::text").extract()
            book_link = link.css("h3 a::attr(href)").extract()











            items["book_title"] = book_title
            items['book_author'] = book_author
            items['year'] = year
            items['language'] = language
            items['file_type_size'] = file_type_size
            items['rate_interest'] = [rate_interest[i].replace('\n',"").strip() for i in range(len(rate_interest))]
            items['rate_quality'] = [rate_quality[i].replace('\n',"").strip() for i in range(len(rate_quality))]
            items['book_link'] = ["https://tr.eg1lib.org" + i for i in book_link]




            yield items


        next_page ="https://eg1lib.org/s/python?page="+str(ZlibSpiterSpider.page_number)
        if ZlibSpiterSpider.page_number < 11:
            ZlibSpiterSpider.page_number +=1
            yield response.follow(next_page, self.parse)

