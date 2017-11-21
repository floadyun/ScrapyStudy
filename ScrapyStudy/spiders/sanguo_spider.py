import scrapy
from bs4 import BeautifulSoup
#爬取三国演义百度百科人名
class sanguo(scrapy.Spider):
    name = 'sanguo'
    start_urls = ['https://baike.baidu.com/item/%E4%B8%89%E5%9B%BD%E6%BC%94%E4%B9%89/5782?fr=aladdin#4_1']

    def parse(self, response):
        soup = BeautifulSoup(response.body, 'lxml')
        table = soup.findAll('table', attrs={'log-set-param': "table_view"})[1]
        trs = table.contents
        print(trs)
        for tr in trs:
            tds = tr.contents
            if len(tds) == 2:
                td = tr.contents[1]
            elif len(tds) == 3:
                td = tr.contents[2]
            for a in td.contents:
                if(a.name==  'a'):
                    print(a.string)

