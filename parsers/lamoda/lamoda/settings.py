BOT_NAME = "lamoda"

SPIDER_MODULES = ["lamoda.spiders"]
NEWSPIDER_MODULE = "lamoda.spiders"

ROBOTSTXT_OBEY = False

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

CONCURRENT_REQUESTS_PER_DOMAIN = 5

DOWNLOAD_DELAY = 1

FEED_EXPORT_ENCODING = "utf-8-sig"

ITEM_PIPELINES = {
    "lamoda.pipelines.LamodaPipeline": 300,
}