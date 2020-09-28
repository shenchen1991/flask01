from flask import Flask, Response

import settings

app = Flask(__name__)
app.config.from_object(settings)

data = {'a': 'bj', 'b': 'nj'}


@app.route('/')
def hello_world():
    return 'Hello World!1q11'


def index():
    return 'index'


@app.route('/getCity/<key>')
def get_city(key):
    return data.get(key)


@app.route('/add/<int:key>')
def add(key):
    return str(key), 200


@app.route('/index/<path:path>')
def index(path):
    return Response(str(path))


@app.route('/test/<uuid:uid>')
def test(uid):
    return uid


app.add_url_rule('/index', view_func=index)

if __name__ == '__main__':
    app.run(port=8081)
