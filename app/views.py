from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    event_title = 'Miguel'
    return render_template('index.html', event_title=event_title)
