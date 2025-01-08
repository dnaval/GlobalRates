from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
import warnings
warnings.filterwarnings('ignore','.*FSADeprecationWarning*')

def config():
    load_dotenv()

config()

app = Flask(__name__)

#CSRF_Token
app.config['SECRET_KEY'] = os.getenv('app_secret')

# Define your database credentials
username = os.getenv("MYSQL_USER")
password = os.getenv("MYSQL_PASSWORD")
host = os.getenv("MYSQL_HOST")  # or your database server's IP
port = os.getenv("MYSQL_PORT")  # Default MySQL port
database = os.getenv("MYSQL_DATABASE")

#MySQL DB CONN
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}"
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

#DB INSTANCE
db = SQLAlchemy(app)

from gr import routes