from models import *

from faker import Faker

faker = Faker()


def seed():
    collection = Collection(title=faker.word().capitalize())

    for i in range(5):
        item = CollectionItem(name=faker.word())
        collection.items.append(item)
        db.session.add(item)

    db.session.add(collection)
    db.session.commit()
    print('Seeding successful.')


if __name__ == '__main__':
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    db.reflect()
    db.drop_all()
    db.create_all()

    seed()
    print('Data ready. Time to code!')
