import os

from time import sleep

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger


def run_spider() -> None:
    os.system("scrapy crawl keng_ru")


if __name__ == "__main__":
    sleep(5)
    run_spider()

    scheduler = BlockingScheduler()

    scheduler.add_job(run_spider, "cron", hour="11")
    scheduler.start()