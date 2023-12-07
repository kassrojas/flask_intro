from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<username>/<int:age>') # @app.route is a decorator
def hello_world(username=None, age=None):
    return render_template('helloworld.html', name=username, age=age)


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/anotherroute')
def another_route():
    return 'This is another route that you were able to access!'


@app.route('/favicon.ico')
def sub_sub_route():
    return 'You have accessed localhost/anotherroute/subroute/subsubroute because of flask! Yay!'