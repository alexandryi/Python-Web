import json

class QuotesPipeline:
    def open_spider(self, spider):
        if spider.name == "quotes":
            self.file = open('qoutes.json', 'w', encoding='utf-8')
            self.file.write('[')
            self.first = True
        elif spider.name == "authors":
            self.file = open('authors.json', 'w', encoding='utf-8')
            self.file.write('[')
            self.first = True

    def close_spider(self, spider):
        self.file.write(']')
        self.file.close()

    def process_item(self, item, spider):
        if not self.first:
            self.file.write(',')
        else:
            self.first = False
        line = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(line)
        return item
