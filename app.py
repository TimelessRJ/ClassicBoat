from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/economic_calendar')
def economic_calendar():
	return render_template('economic_calendar.html')

#omittable
if __name__ == "__main__":
	app.run(debug=True)