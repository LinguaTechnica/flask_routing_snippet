from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

CATEGORIES = ['generic', 'super', 'ultra', 'normal']

collections_items = db.Table('collections_items',
                             db.Column('item_id', db.Integer, db.ForeignKey('collection_items.id')),
                             db.Column('collection_id', db.Integer, db.ForeignKey('collections.id')))


class ModelMixin:
    def save(self):
        db.session.add(self)
        db.session.commit()


class Collection(ModelMixin, db.Model):
    __tablename__ = 'collections'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    items = db.relationship('CollectionItem', secondary='collections_items')

    def __repr__(self):
        return f'<Collection {self.id} | {self.title}>'


class CollectionItem(ModelMixin, db.Model):
    __tablename__ = 'collection_items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    category = db.Column(db.String)

    def __repr__(self):
        return f'<CollectionItem {self.id} | {self.name}>'


def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///collections'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':
    # An application context is required to connect to the database!
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    # Create tables ...
    db.reflect()
    db.drop_all()
    db.create_all()
    print('Connected to database.')
