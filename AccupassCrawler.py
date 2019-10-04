import requests
import logging
from lxml import etree
import json

class AccupassCrawler(object):
    def __init__(self):
        self.url = 'https://old.accupass.com/search/changeconditions/r/0/0/0/0/4/{}/00010101/99991231'

    def start_crawl(self, page):
        with open('example/raw_data.txt', 'w', encoding='UTF-8') as out:
            for i in range(page):
                req = requests.get(self.url.format(i))
                doc = etree.HTML(req.content.decode('utf-8'))
                all_title = [json.loads(p)['name'] for p in doc.xpath('//*[@class="col-xs-12 col-sm-6 col-md-4"]/div/@event-row')]
                for title in all_title:
                    out.write('{}\n'.format(title))

if __name__ == '__main__':
    crawler = AccupassCrawler()
    crawler.start_crawl(20)