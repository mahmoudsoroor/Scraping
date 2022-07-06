import scrapy

from ..items import StackMachineItem

class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['stackoverflow.com']
    start_urls = [
        'https://stackoverflow.com/questions?tab=votes&page=1'
    ]

    page_number = 2

    def parse(self, response):

        items = StackMachineItem()

        title_question= []
        link_answer= []
        tags = []


        post = response.css("div.js-post-summary")
        for p in post:
            title = p.css(".s-link").css('::text').extract()
            title_question.append(str(title[0]))
            link = p.css(".s-link::attr(href)").extract()
            link_answer.append(str(link[0]))
            tag = p.css(".mt0::text").extract()
            tags.append(str([','.join(tag)][0]))


        dates = response.css(".relativetime::text").extract()
        views = response.css(".is-supernova .s-post-summary--stats-item-number").css('::text').extract()
        votes = response.css('.s-post-summary--stats-item__emphasized .s-post-summary--stats-item-number').css("::text").extract()



            # for i in range(len(title_question)):
        items['title_question'] = title_question
        items['link_answer'] = ["https://stackoverflow.com"+i for i in link_answer]
        items['views'] = views
        items['votes'] = votes
        items['tags'] = tags
        items['dates'] = dates



        yield  items






        # next_page = response.css(".s-pagination--item__clear~ .js-pagination-item+ .js-pagination-item::attr(href)").get()
        #
        # if next_page is not None:
        #     yield response.follow(next_page , self.parse)
        #
        next_page = "https://stackoverflow.com/questions?tab=votes&page=" + str(SpiderSpider.page_number)
        if SpiderSpider.page_number < 251:
            SpiderSpider.page_number += 1
            yield response.follow(next_page, self.parse)
