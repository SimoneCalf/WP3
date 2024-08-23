from flask import Flask, render_template, request, jsonify, session
from routes.student import student_bp
from routes.teacher import teacher_bp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models.sql import *
import json
import secrets

# C:\Users\simon\OneDrive\Documenten\AD software development\Werkplaats_3_herkansing\inhaal-wp3-actiontypes-SimoneCalf\WebApp\dump
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Unieke geheime sleutel voor sessies
app.register_blueprint(student_bp, url_prefix='/student')
app.register_blueprint(teacher_bp, url_prefix='/teacher')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/wp3'
sqlalchemy = SQLAlchemy(app)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'wp3'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

# data actiontype statements
with open('json/actiontype_statements.json') as file:
    data = json.load(file)

# endpint to get all actiontype statements
@app.route('/api/actiontype_statements', methods=['GET'])
def get_actiontype_statements():
    return jsonify(data)

# endpoint to get a specific actiontype statement
@app.route('/api/actiontype_statements/<int:statement_number>', methods=['GET'])
def get_actiontype_statement(statement_number):
    for statement in data:
        if statement['statement_number'] == statement_number:
            return jsonify(statement)
    return jsonify({'message': 'Statement not found'}), 404

# home page
@app.route('/')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)