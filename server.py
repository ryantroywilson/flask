from flask import Flask, render_template
app = Flask(__name__)

@app.route ('/')
def index():
	return render_template("index.html", phrase='Hello', times=4, name = 'Ryan')
app.run(debug=True)
