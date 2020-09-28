from flask import Flask, render_template, request, redirect, url_for

import settings

app = Flask(__name__)
app.config.from_object(settings)


@app.route('/', endpoint='index2')
def hello_world():
    return 'Hello World!1q11'


def index():
    return 'index'


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register2', methods=['get', 'post'])
def register2():
    print(request.full_path)
    print(request.path)
    print(request.args)
    print(request.args.get('username'))
    return redirect(url_for('index2'))


app.add_url_rule('/index', view_func=index)

if __name__ == '__main__':
    app.run(port=8081)
