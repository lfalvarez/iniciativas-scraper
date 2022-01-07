from scrapy.crawler import CrawlerProcess

from iniciativas.spiders.iniciativas_list_spider import IniciativasListScrapy

process = CrawlerProcess(settings={
    "FEEDS": {
        "file.csv": {"format": "csv"},
    },
})

process.crawl(IniciativasListScrapy)
process.start()