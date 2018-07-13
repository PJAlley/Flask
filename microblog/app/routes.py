from flask import render_template
from app import app

@app.route('/')
@app.route('/index')

def index():
    user = {'username': 'Timmy'}
    posts = [
        {
          'author': {'username': 'John'},
          'body': "I don't think we're in Kansas anymore...thank God."
        },
        {
          'author': {'username': 'Jane'},
          'body': "Then where are we, Oklahoma?"
        }
    ]
    return render_template('index.html', user = user)

