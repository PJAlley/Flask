from flask import render_template
from app import app
from app.forms import LoginForm

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
    return render_template('index.html', user = user, posts = posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)
