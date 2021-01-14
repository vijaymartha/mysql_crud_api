from app import app
from flaskext.mysql import MySQL

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = ''
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)






# from flask_mongoengine import MongoEngine

# db = MongoEngine()

# def initialize_db(app):
#     db.init_app(app)