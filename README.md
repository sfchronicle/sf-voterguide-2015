# SF voterguide
Our mobile-first voter guide for the 2015 SF local election

## Requirements
- Python 2.7.x
- Node.js 0.12
  - uglifyjs (`npm install -g uglifyjs`)
  - clean-css (`npm install -g cleancss`)
  - Bower and Grunt (`$ npm install -g grunt-cli bower`)

## Installation
```bash
$ git clone git@github.com:sfchronicle/sf-voterguide-2015.git
$ cd sf-voterguide-2015
$ mkvirtualenv sf-voterguide-2015
$ pip install -r requirements.txt && npm install && bower install
```

### Setup database
```bash
$ python createdb.py
$ python migratedb.py db init
$ python migratedb.py db migrate
$ grunt serve  # start server, run grunt task and open app at http://127.0.0.1:5000
```

### Migrations
We're using [flask-migrate](https://flask-migrate.readthedocs.org/en/latest/) to add db migrations to our SQLite database. If you add a new field to models.py or create a new model, you an update the database schema by running:
```bash
$ python migratedb.py db migrate
$ python migratedb.py db upgrade
```

### Deployment
```bash
$ python deploy.py
```
