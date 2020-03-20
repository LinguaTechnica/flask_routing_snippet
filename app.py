import os

from flask import Flask, render_template, redirect, request

from models import CollectionItem, Collection

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secretzzz')


@app.route('/')
def home():
    collections = Collection.query.all()
    return render_template('index.html', collections=collections)


@app.route('/new_collection')
def collection_form():
    return render_template('collections/collection_form.html')


@app.route('/collections', methods=['POST'])
def create_collection():
    collection = Collection(**request.form)
    collection.save()
    return redirect(f'/collection/{collection["id"]}')


@app.route('/collections/<int:collection_id>')
def collection_detail(collection_id):
    collection = Collection.query.get(collection_id)

    return render_template('collections/detail.html', collection=collection)


@app.route('/collections/<int:collection_id>/items', methods=['POST'])
def create_item(collection_id):
    collection = Collection.query.get(collection_id)
    item = CollectionItem(**request.form)
    collection.items.append(item)
    collection.save()

    return redirect(f'/collections/{collection_id}')


if __name__ == '__main__':
    app.run(debug=True)
