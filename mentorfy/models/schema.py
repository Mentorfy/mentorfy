from mongoengine import Document

class User(Document):
    email = StringField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    skills = ListField(StringField())
    password = StringField(max_length=50)
    intentions = ListField(StringField())

