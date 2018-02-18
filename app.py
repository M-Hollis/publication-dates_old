from flask import Flask, render_template, request

import parameters as pars
import script


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('base.html')


@app.route('/', methods=['POST'])
def form_post():
#https://stackoverflow.com/questions/12277933/send-data-from-a-textbox-into-flask
	journal = request.form['journal'].upper()
	num_articles = request.form['num_articles']

	if pars.valid(journal, num_articles):
		script.run(journal, num_articles)
	else:
		return render_template('input_error.html')

	return "Complete!"


if __name__ == "__main__":
    app.run()
