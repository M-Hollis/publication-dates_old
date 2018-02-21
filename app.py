from flask import Flask, render_template, request, make_response

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
		result = q.enqueue(script.run, journal, num_articles)
	else:
		return render_template('input_error.html')

	return "Compiling results..."


@app.route('/download')
def download():
    csv = """"REVIEW_DATE","AUTHOR","ISBN","DISCOUNTED_PRICE"
"1985/01/21","Douglas Adams",0345391802,5.95
"1990/01/12","Douglas Hofstadter",0465026567,9.95
"1998/07/15","Timothy ""The Parser"" Campbell",0968411304,18.99
"1999/12/03","Richard Friedman",0060630353,5.95
"2004/10/04","Randel Helms",0879755725,4.50"""
    response = make_response(csv)
    response.headers["Content-Disposition"] = "attachment; filename=books.csv"
    return response


if __name__ == "__main__":
    app.run()
