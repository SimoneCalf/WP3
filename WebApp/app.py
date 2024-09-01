from flask import Flask, render_template, request, jsonify, session
from routes.student import student_bp
from routes.teacher import teacher_bp
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models.sql import *
from models import sql
import json
import secrets

# C:\Users\simon\OneDrive\Documenten\AD software development\Werkplaats_3_herkansing\inhaal-wp3-actiontypes-SimoneCalf\WebApp\dump
app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # Unieke geheime sleutel voor sessies
app.register_blueprint(student_bp, url_prefix='/student')
app.register_blueprint(teacher_bp, url_prefix='/teacher')

# MySQL configuration
app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'actiontypes_wp3'
app.config['MYSQL_DB'] = 'wp3'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
app.config['MYSQL_PORT'] = 3307

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

# retrieve statement api
@app.route('/api/student/<student_number>/statement', methods=['GET'])
def get_student_statement(student_number):
    if not sql.get_student(student_number=int(student_number)):
        return  jsonify({'message': 'Student not found'}), 400

    get_max_statement_id = sql.get_max_statement_id(student_number=int(student_number))
    
    if get_max_statement_id == 20:
        # return a 400 error if the student has already answered all the questions
        return jsonify({'message': 'Student has already answered all questions'}), 400
    
    # get the question for the next statement
    first, second = sql.get_question(get_max_statement_id + 1)


    returner = {
        "statement_number":get_max_statement_id + 1,
        "statement_choices":[
      {
         "choice_number":first['choice_id'],
         "choice_text": first['choice_text']
      },
      {
         "choice_number":second['choice_id'],
         "choice_text":second['choice_text']
      }
   ]
    }


    if returner:
        return jsonify(returner)
    return jsonify({'message': 'Student not found'}), 404

# save student choice api
@app.route('/api/student/<student_nummer>/statement/<stelling_id>', methods=['POST'])
def save_student_choice(student_nummer, stelling_id):
    student_number = int(student_nummer)
    statement_id = int(stelling_id)
    choice = request.json.get('statement_choice')
    if not sql.get_student(student_number=student_number):
        return jsonify({'message': 'Student not found'}), 404
    if not sql.get_question(statement_id):
        return jsonify({'message': 'Statement not found'}), 404
    if not choice:
        return jsonify({'message': 'statement_choice not found'}), 400
    sql.add_answer(student_number, statement_id, choice)
    return jsonify({ 'result': 'ok'}), 200



# home page
@app.route('/')
def home():
    return render_template('home.html')



if __name__ == '__main__':
    app.run(debug=True)