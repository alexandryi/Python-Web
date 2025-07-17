from mongoengine import Document, StringField, ReferenceField, ListField, connect

connect(
    db="quotes_db",
    host="mongodb+srv://demaniyas:Al6loversme13_@cluster0.slhasvk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", 
)

class Author(Document):
    fullname = StringField(required=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField(StringField())
    author = ReferenceField(Author, required=True)
    quote = StringField(required=True)
