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

@app.route('/')
def home():
    return render_template('home.html')


def load_students_to_db(json_file):
    with app.app_context():
        conn = mysql.connection
        cursor = conn.cursor()
        try:
            with open(json_file) as file:
                data = json.load(file)

            for student in data:
                cursor.execute("INSERT INTO students (student_class, student_name, student_number) VALUES (%s, %s, %s)",
                               (student['student_class'], student['student_name'], student['student_number']))
            conn.commit()
        finally:
            cursor.close()

def load_data_to_statement_numbers_table(json_file):
    with app.app_context():
        conn = mysql.connection
        cursor = conn.cursor()
        try:
            with open(json_file) as file:
                data = json.load(file)
                # delete all data from statement_numbers
                #cursor.execute('DELETE FROM statement_numbers')
                for statement in data:
                    statement_number = statement['statement_number']
                    print(f'dit is de statement_number: {statement_number}')
                    # get all the statement_numbers from the table statement_numbers
                    cursor.execute('SELECT statement_number FROM statement_numbers WHERE statement_number = %s', (statement_number,))
                    result = cursor.fetchall()
                    print(f'info about statement_numbers: {result}')
                    # check if the statement_number already exists
                    # Controleren of 1 voorkomt in de sleutel 'statement_number'
                    if any(item['statement_number'] == statement_number for item in data):
                        print(f"fDe waarde: {statement_number} komt voor in de tabel statement_numbers")
                    else:
                # insert the statement_number into the table statement_numbers
                cursor.execute(
                    "INSERT INTO statement_numbers (statement_number) VALUES (%s)",
                    (statement_number,)
                )
                    
                conn.commit()
        except Exception as e:
            print(f"Error: {e}")
            conn.rollback()
        finally:
            cursor.close()

def load_actiontype_statements_to_db(json_file):
    with app.app_context():
        conn = mysql.connection
        cursor = conn.cursor()
        try:
            with open(json_file) as file:
                data = json.load(file)
                print('hallo')
                for statement in data:
                    statement_number = statement['statement_number']
                    print(f'dit is de statement_number: {statement_number}')
                    
                    # Check if the statement_number already exists
                    cursor.execute(
                        "SELECT id FROM statement_numbers WHERE statement_number = %s",
                        (statement_number,)
                    )
                    existing_id = cursor.fetchone()
                    print(f'existing_id: {existing_id}')
                    if existing_id:
                        # If it exists, use the existing ID
                        statement_number_id = existing_id[0]
                        print(f'Found existing statement_number with ID: {statement_number_id}')
                    else:
                        print('halllllll')
                        # Insert data into the table `statement_numbers`
                        cursor.execute(
                            "INSERT INTO statement_numbers (statement_number) VALUES (%s)",
                            (statement_number,)
                        )
                        conn.commit()
                        
                        # Retrieve the ID of the inserted statement_number
                        statement_number_id = cursor.lastrowid
                        print(f'Inserted statement_number with ID: {statement_number_id}')
                # for statement in data:
                #     statement_number = statement['statement_number']
                #     print(f'dit is de statement_number: {statement_number}')
                    
                    
                #     # Insert data into the table `statement_numbers`
                #     cursor.execute(
                #         "INSERT INTO statement_numbers (statement_number) VALUES (%s)",
                #         (statement_number,)
                #     )

                #     # check if the data in the table statement_numbers is inserted

                    
                #     # Retrieve the ID of the inserted statement_number
                #     statement_number_id = cursor.lastrowid
                #     print(f'Inserted statement_number with ID: {statement_number_id}')

                for statement in data:
                    for choice in statement['statement_choices']:
                        choice_number = choice['choice_number']
                        print(f'dit is de choice_number: {choice_number}')
                        choice_text = choice['choice_text']
                        print(f'dit is de choice_text: {choice_text}')
                        choice_result = choice['choice_result']
                        print(f'dit is de choice_result: {choice_result}')
                        cursor.execute(
                            "INSERT INTO statement_choices (statement_number_id, choice_number, choice_text, choice_result) VALUES (%s, %s, %s, %s)",
                            (statement_number, choice_number, choice_text, choice_result)
                        )
                conn.commit()   
        except Exception as e:
            print(f"Error: {e}")
            conn.rollback()
        finally:
            cursor.close()

@app.route('/upload_students')
def upload_students():
    load_students_to_db('json/students.json')
    return jsonify({'message': 'Students loaded successfully'}), 200

@app.route('/upload_statement_numbers')
def upload_statement_numbers():
    load_data_to_statement_numbers_table('json/actiontype_statements.json')
    return jsonify({'message': 'Statement numbers loaded successfully'}), 200    

@app.route('/upload_actiontypes')
def upload_actiontypes():
    load_actiontype_statements_to_db('json/actiontype_statements.json')
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM statement_choices')
    result = cursor.fetchall()
    cursor.close()
    print(f'info about statementchoices: {result}')
    return jsonify({'message': 'Actiontypes loaded successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)