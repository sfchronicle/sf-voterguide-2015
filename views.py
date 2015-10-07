from flask import render_template  #, redirect, url_for

from app import app, db
from models import Measure, Candidate


@app.route('/')
def index():
    measures = Measure.query.all()
    mayor = Candidate.query.filter_by(type='mayor')
    sheriff = Candidate.query.filter_by(type='sheriff')
    d3 = Candidate.query.filter_by(type='d3')

    return render_template(
        'index.html',
        title='index',
        measures=measures,
        sheriff=sheriff,
        mayor=mayor,
        d3=d3
    )
