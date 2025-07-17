import subprocess
from hm9.spiders.quotes_spider import QuotesSpider


def run_spiders():
    subprocess.run(['scrapy', 'crawl', 'quotes'])
    subprocess.run(['scrapy', 'crawl', 'authors'])

def load_data():
    subprocess.run(['python', 'load_data.py'])

if __name__ == '__main__':
    run_spiders()
    load_data()
