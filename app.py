from flask import Flask, render_template, request

from rq import Queue
from worker import conn

import parameters as pars
import script


app = Flask(__name__)

q = Queue(connection=conn)


@app.route("/")
def index():
    return render_template('base.html')


@app.route('/', methods=['POST'])
def form_post():
#https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask
	journal = request.form['journal'].upper()
	num_articles = request.form['num_articles']

	if pars.valid(journal, num_articles):
		# result = q.enqueue(count_words_at_url, 'http://heroku.com')
		result = q.enqueue(script.run, journal, num_articles)
	else:
		return render_template('input_error.html')

	return "Complete!"


if __name__ == "__main__":
    app.run()
