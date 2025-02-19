from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db) 
# creates history of database, 
# syncs models and database, better manage database. 
# Allows for changes to be made without having to recreate database each time.
CORS(app) 

from app import routes, models