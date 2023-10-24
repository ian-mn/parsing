from datetime import date
from urllib.parse import urljoin

import scrapy
from bs4 import BeautifulSoup
from keng_ru.constants import ALLOWED_DOMAINS, BASE_URL, START_URL
from keng_ru.items import KengRuItem


class KengRuSpider(scrapy.Spider):
    name = "keng_ru"
    allowed_domains = ALLOWED_DOMAINS
    start_url = START_URL

    def start_requests(self):
        yield scrapy.Request(
            url=self.start_url,
            callback=self.parse_brands,
        )

    def parse_brands(self, response):
        soup = BeautifulSoup(response.text, features="lxml")
        brand_list = soup.find("div", {"class": "brands__alphalist"})
        brands = brand_list.find_all("a", {"class": "ul__item--link"})
        for brand in brands:
            brand_url = urljoin(BASE_URL, brand["href"])
            yield scrapy.Request(
                url=brand_url,
                callback=self.parse_pages,
            )

    def parse_pages(self, response):
        soup = BeautifulSoup(response.text, features="lxml")
        pages = soup.find_all("a", {"class": "paging__item--link"})

        if len(pages) == 0:
            yield scrapy.Request(
                url=response.url,
                callback=self.parse_items,
            )
        else:
            for page, _ in enumerate(pages[1:-1], start=1):
                brand_page_url = urljoin(response.url, f"?pec=60&page={page}")
                yield scrapy.Request(
                    url=brand_page_url,
                    callback=self.parse_items,
                )

    def parse_items(self, response):
        soup = BeautifulSoup(response.text, features="lxml")
        items = soup.find_all("li", {"class": "js-catalog-item"})

        for item in items:
            url = item.find("a")["href"]
            title = item.find(
                "a", {"class": "gtag-item-click block__category--link"}
            ).text.replace("'", "")
            art_start = "арт. "
            art_end = " |"
            description = item.find("img")["title"]
            article = description[
                description.rfind(art_start)
                + len(art_start) : description.rfind(art_end)
            ]
            article = "".join(c for c in article if c.isalnum() or c == " ").upper()
            brand = item["data-brand"]
            category = item["data-category"]

            yield scrapy.Request(
                url=urljoin(BASE_URL, url),
                callback=self.parse_sizes,
                cb_kwargs=dict(
                    title=title,
                    article=article,
                    description=description,
                    brand=brand,
                    category=category,
                ),
                meta={
                    "proxy": "http://a1b449d13a393beebe0237cdd85ef816c5240b90:autoparse=true@proxy.zenrows.com:8001",
                },
            )

    def parse_sizes(self, response, title, article, description, brand, category):
        data = response.json()
        sizes = data[3]

        for _, value in sizes.items():
            yield KengRuItem(
                {
                    "date": date.today().strftime("%Y-%m-%d"),
                    "article": article,
                    "title": title,
                    "size": value.get("SIZE_TEXT", "NS"),
                    "category": category,
                    "brand": brand,
                    "current_price": value.get("PRICE", 0),
                    "first_price": value.get("OLD_PRICE", 0),
                    "price_classic": value.get("PRICE_CLASSIC", 0),
                    "price_celebrity": value.get("PRICE_CELEBRITY", 0),
                    "price_prestige": value.get("PRICE_PRESTIGE", 0),
                    "price_platinum": value.get("PRICE_PLATINUM", 0),
                    "price_elite": value.get("PRICE_ELITE", 0),
                    "price_brilliant": value.get("PRICE_BRILLIANT", 0),
                    "qty": value.get("QUANTITY", 0),
                    "url": response.url,
                }
            )
