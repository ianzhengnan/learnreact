
from flask import Flask
from flask import request, render_template, send_from_directory
from flask import json

import mysql.connector


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
	return render_template('index.html')


@app.route('/api/comments', methods=['GET', 'POST'])
def handle():
	if request.method == 'POST':
		try:
			saveData(request.form['id'], request.form['author'], request.form['text'])
			return json.dumps({"status": "ok"})
		except Exception as e:
			print(e)
		
	elif request.method == 'GET':
		try:
			conn = mysql.connector.connect(user='root', password='1234567', database='test')
			cursor = conn.cursor()
			cursor.execute('select * from comments')
			values = cursor.fetchall()
			cursor.close()
			conn.close()
		except Exception as e:
			print(e)

		output = []
		if values:
			for item in values:
				output.append({'id':item[0], 'author': item[1], 'text': item[2]})

		return json.dumps(output) if values else json.dumps()


def saveData(id, author, text):
	try:
		conn = mysql.connector.connect(user='root', password='1234567', database='test')
		cursor = conn.cursor()
		cursor.execute('insert into comments (id, author, text) values (%s, %s, %s)', 
			[id, author, text])
		conn.commit()
		cursor.close()
		conn.close()
	except Exception as e:
		print(e)
		raise


if __name__ == '__main__':
	app.run()