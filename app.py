from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

COLLECTIONS = [
    {'title': 'First Collection', 'id': 1}
]
COUNTER = 1


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/new_collection')
def collection_form():
    return render_template('collection_form.html')


@app.route('/collections', methods=['POST'])
def collection_form():
    global COUNTER

    COUNTER += 1
    collection = {'title': request.form.get('title'), 'id': COUNTER}
    session['collection_id'] = COUNTER
    return redirect(f'/collection/{collection["id"]}')


if __name__ == '__main__':
    app.run()
