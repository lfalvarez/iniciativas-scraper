from scrapy.crawler import CrawlerProcess

from iniciativas.spiders.iniciativas_list_spider import IniciativasListScrapy

process = CrawlerProcess(settings={
    "FEEDS": {
        "file.csv": {
            "format": "csv",
            "fields": ['id', 'apoyos', 'titulo', 'categoria', 'problema', 'propuesta_articulado', 'que_debe_contemplar',
                       'situacion_ideal', 'propone', 'url']
        },
    },
})

process.crawl(IniciativasListScrapy)
process.start()
