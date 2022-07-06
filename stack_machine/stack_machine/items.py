# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StackMachineItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title_question = scrapy.Field()
    link_answer = scrapy.Field()
    dates = scrapy.Field()
    tags = scrapy.Field()
    views = scrapy.Field()
    votes = scrapy.Field()


