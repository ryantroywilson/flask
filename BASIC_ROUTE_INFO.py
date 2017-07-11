"""
BASIC ROUTES INFORMATION
Basic Routes
Routes are an essential part of any web application. 

Every route has two parts:

HTTP Verb (GET, POST, PUT, PATCH, DELETE)
URL
For the next couple of examples, we are going to focus only on GET routes. But what is a route? A route is a handler for a particular HTTP request. When an HTTP request hits a server the server checks to see whether it can handle the request (ie. a route).   The route then runs and sends an appropriate HTTP response. 

Let's take a look back at our Hello Flask example:

/hello_flask/templates/index.html
<html>
  <body>
    <p>Hello Flask!</p>
  </body>
</html>
Copy
/hello_flask/hello.py
from flask import Flask, render_template  # Import Flask to allow us to create our app, and import
                                          # render_template to allow us to render index.html.
app = Flask(__name__)                     # Global variable __name__ tells Flask whether or not we
                                          # are running the file directly or importing it as a module.
@app.route('/')                           # The "@" symbol designates a "decorator" which attaches the
                                          # following function to the '/' route. This means that
                                          # whenever we send a request to localhost:5000/ we will run
                                          # the following "hello_world" function.
def hello_world():
  return render_template('index.html')    # Render the template and return it!
app.run(debug=True)                       # Run the app in debug mode.
Copy
Here you can see that we are handling the '/' route with the hello_world function which renders the index.html template. Here the HTTP verb is "GET". 

ALL ROUTES ARE DEFAULT TO GET! 
If no route is explicitly mentioned, it is a GET route. GET routes will mostly be used for serving pages or rendering templates. We'll learn more about POST routes in the later chapters.

Now let's create a route that serves another page!

Add the following route to your hello.py file:

@app.route('/success')
def success():
  return render_template('success.html')
Copy
Now create the success.html file.

/hello_flask/templates/success.html
<html>
  <body>
    <p>Yay you successfully created another GET route that serves a page!</p>
  </body>
</html>
Copy
Make sure you understand how to add routes that serve pages before moving on to the assignment.

Route Structure
When creating generic routes we write something like this:

@app.route('/some_route')
def some_function_name():
  // your code here
Copy
The above route would be triggered when a user requests:

localhost:5000/some_route
In other words, our route rules define what comes after the initial forward-slash. When a request matching our routing rule is received by the server. The function that immediately follows the @app.route('/some_route') is invoked.
"""