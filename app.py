from flask import Flask, render_template, request, send_file

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
	journal = request.form['journal'].upper()
	num_articles = request.form['num_articles']

	if pars.valid(journal, num_articles):
		result = q.enqueue(script.run, journal, num_articles)
	else:
		return render_template('input_error.html')

	return render_template('processing.html')


@app.route('/download')
def download():
	try:
		return send_file(results_filename, mimetype="text/csv", as_attachment=True)
# NB DOESN'T TAKE JOURNAL NAME FROM WEB INPUT
	except Exception:
		return render_template('download_error.html')


if __name__ == "__main__":
    app.run()
