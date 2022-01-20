from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup

from iniciativas.items import IniciativasItem


class IniciativasListScrapy(CrawlSpider):
    name = "iniciativas"
    allowed_domains = ['iniciativas.chileconvencion.cl', ]
    start_urls = ["https://iniciativas.chileconvencion.cl/m/iniciativa_popular/", ]

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css='#iniciativas div.iniciativa h1', ), callback='parse_item'),
    )

    def parse_item(self, response):
        item = IniciativasItem()
        text_id = response.css('.objeto h2::text').get()
        apoyo_text = response.css('#apoyo strong::text').get().replace('.', '').replace(' ', '')
        id_iniciativa = int(text_id.replace('Iniciativa Nº ', '').replace('.', ''))
        item['id'] = id_iniciativa
        item['titulo'] = response.css('.objeto h1::text').get()
        item['apoyos'] = int(apoyo_text)
        proposing_org = response.xpath("//div[contains(@class, 'org')]")
        if proposing_org:
            org_name = BeautifulSoup(proposing_org[0].get()).text.strip()
            item['propone'] = org_name
        propuesta_parrafos = response.xpath('//*[@id="propuesta"]/p')
        item['problema'] = BeautifulSoup(propuesta_parrafos[0].get(), "lxml").text
        item['situacion_ideal'] = BeautifulSoup(propuesta_parrafos[1].get(), "lxml").text
        item['que_debe_contemplar'] = BeautifulSoup(propuesta_parrafos[2].get(), "lxml").text
        propuesta_articulado = BeautifulSoup(propuesta_parrafos[4].get(), "lxml").text
        item['propuesta_articulado'] = propuesta_articulado
        categoria = response.xpath('//div[contains(@class,"rainbow")]')
        item['categoria'] = BeautifulSoup(categoria.get(), "lxml").text
        item['url'] = f'https://iniciativas.chileconvencion.cl/m/iniciativa_popular/o/{id_iniciativa}'
        return item



a= '<html><body><div class="org"><p><img alt="Imagen de grupo" class="foto_grupo chica" src="../../../d/g/8659b1e787b5c7bfa6d11e8fa91b965d/perfil_grupo/4f65c38b7baeb965d63195d14289334e.jpg"/></p><p>Coordinadora Nahuelbuta Biobío Constituyente</p></div></body></html>'
