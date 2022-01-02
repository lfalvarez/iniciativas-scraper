# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IniciativasItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    titulo = scrapy.Field()
    apoyos = scrapy.Field()
    problema = scrapy.Field()
    situacion_ideal = scrapy.Field()
    que_debe_contemplar = scrapy.Field()
    propuesta_articulado = scrapy.Field()

