import os

from flask.ext.frozen import Freezer

from app import app, assets
from views import *

BUILD_DIR = os.path.join(os.path.realpath(os.path.dirname(__file__)), 'build')
S3_BUCKET_NAME = 'projects.sfchronicle.com'
PROJECT_NAME = '2015/voterguide/'
freezer = Freezer(app)

def upload_assets():
    print('Uploading ...')
    command = 'aws s3 cp --recursive --acl public-read {} s3://{}/{}'.format(
        BUILD_DIR,
        S3_BUCKET_NAME,
        PROJECT_NAME
    )
    os.system(command)
    print('Project deployed!')

if __name__ == '__main__':
    app.config['DEBUG'] = False
    app.config['ASSETS_DEBUG'] = False

    app.config['FREEZER_RELATIVE_URLS'] = True
    app.config['FLASK_ASSETS_USE_S3']= True
    app.config['S3_BUCKET_NAME'] = S3_BUCKET_NAME
    app.config['S3_USE_HTTPS'] = False

    freezer.freeze()
    upload_assets()
