import scrapy


class LamodaItem(scrapy.Item):
    date = scrapy.Field()
    brand = scrapy.Field()
    article = scrapy.Field()
    category = scrapy.Field()
    current_price = scrapy.Field()
    first_price = scrapy.Field()
    url = scrapy.Field()
