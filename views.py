from flask import render_template  #, redirect, url_for

from app import app, db
from models import Measure


@app.route('/')
def index():
    measures = Measure.query.all()
    return render_template('index.html', title='index', measures=measures)
