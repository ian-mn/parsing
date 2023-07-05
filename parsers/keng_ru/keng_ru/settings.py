BOT_NAME = "keng_ru"

SPIDER_MODULES = ["keng_ru.spiders"]
NEWSPIDER_MODULE = "keng_ru.spiders"

ROBOTSTXT_OBEY = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

CONCURRENT_REQUESTS_PER_DOMAIN = 10

DOWNLOAD_DELAY = 1

FEED_EXPORT_ENCODING = "utf-8-sig"

ITEM_PIPELINES = {
    "keng_ru.pipelines.KengRuPipeline": 300,
}