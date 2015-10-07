import flask_admin as admin
from flask_admin.contrib.sqla import ModelView

from app import app, db
from models import Measure, Candidate

# Admin
admin = admin.Admin(app)
admin.add_view(ModelView(Measure, db.session))
admin.add_view(ModelView(Candidate, db.session))
