from datetime import datetime
from flask import render_template  #, redirect, url_for

from app import app, db
from models import Measure, Candidate


@app.route('/')
def index():
    measures = Measure.query.all()
    mayor = Candidate.query.filter_by(type='mayor')
    sheriff = Candidate.query.filter_by(type='sheriff')
    d3 = Candidate.query.filter_by(type='d3')

    district_attorney = Candidate.query.filter_by(type='da')
    city_attorney = Candidate.query.filter_by(type='ca')
    treasurer = Candidate.query.filter_by(type='treasurer')

    community_college = Candidate.query.filter_by(type='cc')

    return render_template(
        'index.html',
        title='index',
        measures=measures,
        sheriff=sheriff,
        mayor=mayor,
        d3=d3,
        district_attorney=district_attorney,
        city_attorney=city_attorney,
        treasurer=treasurer,
        community_college=community_college,
        publish_date=datetime.now()
    )
