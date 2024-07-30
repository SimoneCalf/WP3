from flask import Flask, render_template, request, jsonify
from routes.student import student_bp
from routes.teacher import teacher_bp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models.sql import *
import json


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
    get_student_info()
    return render_template('home.html')


def load_students_to_db(json_file):
    with app.app_context():
        conn = mysql.connection
        cursor = conn.cursor()
        try:
            with open(json_file) as file:
                data = json.load(file)

            for student in data:
                cursor.execute("INSERT INTO students (studentnumber, name, last_name) VALUES (%s, %s, %s)",
                               (student['studentnumber'], student['name'], student['last_name']))
            conn.commit()
        finally:
            cursor.close()

@app.route('/upload_students')
def upload_students():
    load_students_to_db('students.json')
    return jsonify({'message': 'Students loaded successfully'}), 200



if __name__ == '__main__':
    app.run(debug=True)