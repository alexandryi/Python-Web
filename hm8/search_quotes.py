from models import Author, Quote

def search_quotes():
    while True:
        cmd = input("Введіть команду (name: ..., tag: ..., tags: ..., exit): ").strip()
        if cmd == 'exit':
            break
        if cmd.startswith('name:'):
            name = cmd[5:].strip()
            author = Author.objects(fullname=name).first()
            if author:
                quotes = Quote.objects(author=author)
                for q in quotes:
                    print(q.quote.encode('utf-8').decode('utf-8'))
            else:
                print("Автор не знайдений.")
        elif cmd.startswith('tag:'):
            tag = cmd[4:].strip()
            quotes = Quote.objects(tags=tag)
            for q in quotes:
                print(q.quote.encode('utf-8').decode('utf-8'))
        elif cmd.startswith('tags:'):
            tags = cmd[5:].strip().split(',')
            quotes = Quote.objects(tags__in=tags)
            for q in quotes:
                print(q.quote.encode('utf-8').decode('utf-8'))
        else:
            print("Невірна команда.")

if __name__ == '__main__':
    search_quotes()
