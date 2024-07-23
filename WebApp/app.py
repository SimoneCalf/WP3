from flask import Flask, render_template, request, jsonify
from routes.student import student_bp
from routes.teacher import teacher_bp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models.sql import *


app = Flask(__name__)
app.register_blueprint(student_bp, url_prefix='/student')
app.register_blueprint(teacher_bp, url_prefix='/teacher')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/our_users'
sqlalchemy = SQLAlchemy(app)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'our_users'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)


@app.route('/')
def home():
    get_teacher_info()
    return render_template('home.html')




if __name__ == '__main__':
    app.run(debug=True)