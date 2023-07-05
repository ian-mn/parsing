import scrapy


class KengRuItem(scrapy.Item):
    date = scrapy.Field()
    article = scrapy.Field()
    title = scrapy.Field()
    size = scrapy.Field()
    category = scrapy.Field()
    brand = scrapy.Field()
    current_price = scrapy.Field()
    first_price = scrapy.Field()
    price_classic = scrapy.Field()
    price_celebrity = scrapy.Field()
    price_prestige = scrapy.Field()
    price_platinum = scrapy.Field()
    price_elite = scrapy.Field()
    price_brilliant = scrapy.Field()
    qty = scrapy.Field()
    url = scrapy.Field()

