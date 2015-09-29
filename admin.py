import flask_admin as admin
from flask_admin.contrib.sqla import ModelView

from app import app, db
from models import Measure

# Admin
admin = admin.Admin(app)
admin.add_view(ModelView(Measure, db.session))
