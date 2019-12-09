from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    message = 'Hello, World!'
    return render_template('index.html', message=message)
    