from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/echo', methods=['POST'])
def echo():
    return 'Hello World and hello %s' % request.json['name']


if __name__ == '__main__':
    app.run()
