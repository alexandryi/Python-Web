import json
from models import Author, Quote

def load_authors():
    with open('authors.json', encoding='utf-8') as f:
        authors_data = json.load(f)
    for item in authors_data:
        if not Author.objects(fullname=item['fullname']):
            Author(**item).save()

def load_quotes():
    with open('qoutes.json', encoding='utf-8') as f:
        quotes_data = json.load(f)
    for item in quotes_data:
        author = Author.objects(fullname=item['author']).first()
        if author:
            if not Quote.objects(quote=item['quote']):
                Quote(tags=item['tags'], author=author, quote=item['quote']).save()

