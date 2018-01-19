from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def first_page():
    return render_template("first_page.html", phrase='I love python')

@app.route('/ninjas')
def ninja():
    return render_template('ninja.html')

@app.route('/dojo')
def dojo():
    return render_template('dojo.html')
app.run(debug=True)
