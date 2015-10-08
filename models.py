from datetime import datetime
from app import db

# Create models here


class Measure(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    letter = db.Column(db.String(1))
    title = db.Column(db.String(100))
    description = db.Column(db.Text())
    endorse = db.Column(db.Boolean())
    endorsement_reason = db.Column(db.Text())
    endorsement_url = db.Column(db.String(255))
    endorsement_video_url = db.Column(db.String(100))

    def __unicode__(self):
        return '{} {}'.format(self.letter, self.letter, self.title)

    def __repr__(self):
        return '<Measure {}: {}>'.format(self.letter, self.title)


class Candidate(db.Model):
    TYPES = [
        ('mayor', 'Mayor'),
        ('sheriff', 'Sheriff'),
        ('d3', 'District 3')
    ]
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    image_url = db.Column(db.String(255))
    type = db.Column(db.String(10))
    endorse = db.Column(db.Boolean())

    def __unicode__(self):
        return self.name

    def __repr__(self):
        return '<Candidate: {}>'.format(self.name)
