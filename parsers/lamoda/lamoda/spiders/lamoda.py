import re
from datetime import date
from urllib.parse import urljoin

import scrapy
from bs4 import BeautifulSoup
from lamoda.constants import ALLOWED_DOMAINS, BASE_URL, START_URLS
from lamoda.items import LamodaItem


class LamodaSpider(scrapy.Spider):
    name = "lamoda"
    allowed_domains = ALLOWED_DOMAINS
    start_urls = START_URLS

    def start_requests(self):
        for brand_url in self.start_urls:
            page = 1
            while page <= 10:
                url = f"{brand_url['url']}{page}"
                page += 1
                yield scrapy.Request(
                    url=url,
                    callback=self.parse_page,
                    cb_kwargs=dict(
                        brand=brand_url["brand"],
                    ),
                )

    def parse_page(self, response, brand):
        soup = BeautifulSoup(response.text, features="lxml")
        grid = soup.find("div", {"class": "grid__catalog"})
        if not grid:
            return
        items = grid.find_all("a")
        for item in items:
            item_url = urljoin(BASE_URL, item["href"])
            yield scrapy.Request(
                url=item_url,
                callback=self.parse_item,
                cb_kwargs=dict(
                    brand=brand,
                ),
            )

    def parse_item(self, response, brand):
        soup = BeautifulSoup(response.text, features="lxml")
        keyword = "sku_supplier"
        script = soup.find(text=re.compile(keyword))
        script = script.replace('":"', "")
        l_pos = script.find(keyword) + len(keyword)
        script = script[l_pos:]
        r_pos = script.find('",')

        article = script[:r_pos]
        current_price_soup = soup.find_all(
            "span", {"class": "x-premium-product-prices__price"}
        )
        current_price = current_price_soup[-1].text.replace(" ", "").replace("₽", "")
        first_price = current_price_soup[0].text.replace(" ", "").replace("₽", "")

        cats = soup.find("div", {"id": "breadcrumbs"})
        category = ", ".join([x.text for x in cats.find_all("a")]).replace("\n", "")

        yield LamodaItem(
            date=date.today().strftime("%Y-%m-%d"),
            brand=brand,
            article=article,
            category=category,
            current_price=current_price,
            first_price=first_price,
            url=response.url,
        )
