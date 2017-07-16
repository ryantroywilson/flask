from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def index():
   if 'counter' not in session:
       session['counter'] = 0
   session['counter'] += 1
   return render_template('index.html')

@app.route('/ninja')
def ninja():
 	if 'counter' not in session:
  		session['counter'] = 0
  	session9['counter'] += 2
  	return render_template('ninja.html')

@app.route('/hacker', methods=['POST'])
def reset():
   session.clear()
   return redirect('/hacker')

app.run(debug=True)