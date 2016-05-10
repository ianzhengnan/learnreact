
from flask import Flask
from flask import request, render_template, send_from_directory
from flask import json


app = Flask(__name__, static_url_path='')

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('index.html')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)


@app.route('/api/comments', methods=['GET'])
def get_comments():
	return json.dumps([
  {"id": "1", "author": "Pete Hunt", "text": "This is one comment"},
  {"id": "2", "author": "Jordan Walke", "text": "This is *another* comment"},
  {"id": "3", "author": "Ian Zheng", "text": "This is *my* comment"}
])


if __name__ == '__main__':
	app.run()