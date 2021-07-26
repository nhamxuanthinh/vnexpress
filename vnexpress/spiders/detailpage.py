import scrapy
import logging
from vnexpress.items import VnexpressItem


class DetailSpider(scrapy.Spider):
    name = 'detail'
    allowed_domains = ['vnexpress.net']
    start_urls = ['https://vnexpress.net/vuong-nghi-my-trung-ben-bo-vuc-chien-tranh-lanh-4104368.html']

    # scrapy crawl detail page vnexpress.net
    def parse(self, response):

        TITLE_SELECTOR = '.title-detail::text'
        DATE_SELECTOR = '.date::text'
        DESCRIPTION_SELECTOR = '.description::text'
        CONTENT_SELECTOR = '.Normal::text'

        url = response.url
        title = response.css(TITLE_SELECTOR).extract()
        # existing case have special title -> ignore
        if not title:
            logging.info('title specical')
            exeSQL = VnexpressItem(url=url, title="null", date="null", article="null")
            yield exeSQL

        else:
            logging.info('title OK')
            date = response.css(DATE_SELECTOR).extract()
            description_arr = response.css(DESCRIPTION_SELECTOR).extract()

            article = ""

            # existing case have not description
            if description_arr:
                logging.info('exist description')
                # add space character after description to make pretty article
                description = description_arr[0] + " "
                article += description

            # currently contents of article has been devided into many difference parts -> have to merge string
            contents = response.css(CONTENT_SELECTOR).extract()
            for content in contents:
                article += content

            exeSQL = VnexpressItem(url=url, title=title[0], date=date[0], article=article)
            logging.info('execute SQL.')
            yield exeSQL
