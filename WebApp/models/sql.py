from flask_mysqldb import MySQL
import json
from flask import jsonify


mysql = MySQL()

# query to get all the teacher information
def get_teacher_info():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM teacher')
    result = cursor.fetchall()
    cursor.close()
    return result

# query to get all the student information
def get_student_info():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM students')
    result = cursor.fetchall()
    cursor.close()
    return result

# query to get the hightest question number
def get_max_quetsion_number():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT MAX(id) FROM statement_number')
    result = cursor.fetchall()
    cursor.close()
    if result[0]['MAX(id)'] is None:
        return 0
    return result[0]['MAX(id)']

# query to get the question where the student is at
def get_current_question_number(student_number):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT MAX(statement_id) FROM answer WHERE student_number = %s', (student_number,))
    result = cursor.fetchall()
    cursor.close()
    if result[0]['MAX(statement_id)'] is None:
        return 1
    return result[0]['MAX(statement_id)']

# query to get the student information
def get_student(student_number):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM students WHERE number = %s', (student_number,))
    result = cursor.fetchall()
    cursor.close()
    if result:
        return result[0]
    return False

# query to get all data about the actiontype statements
def get_actiontype_statements():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM choices')
    result = cursor.fetchall()
    cursor.close()
    return result

# get the question
def get_question(statement_number):
    cursor = mysql.connection.cursor()
    query = """
    SELECT 
        sc_a.id AS choice_a_id, sc_a.text AS choice_a_text, sc_a.result AS choice_a_result,
        sc_b.id AS choice_b_id, sc_b.text AS choice_b_text, sc_b.result AS choice_b_result
    FROM 
        statement_number sn
    JOIN 
        statement_choices sc_a ON sn.choice_a_id = sc_a.id
    JOIN 
        statement_choices sc_b ON sn.choice_b_id = sc_b.id
    WHERE 
        sn.id = %s;
    """
    cursor.execute(query, (statement_number,))
    result = cursor.fetchall()
    if not result:
        cursor.close()
        return False
    else:
        first_choice = {
            'choice_id': result[0]['choice_a_id'],
            'choice_text': result[0]['choice_a_text'],
            'choice_result': result[0]['choice_a_result']
        }
        second_choice = {
            'choice_id': result[0]['choice_b_id'],
            'choice_text': result[0]['choice_b_text'],
            'choice_result': result[0]['choice_b_result']
        }
        cursor.close()
        return first_choice, second_choice


# add the choice result for the statement number to the database for the student that is logged in
def add_answer(student_number, statement_id, choice_id):
    cursor = mysql.connection.cursor()
    query = 'INSERT INTO answer (student_number, statement_id, choice_id) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE choice_id = %s'
    cursor.execute(query, (student_number, statement_id, choice_id, choice_id,))
    mysql.connection.commit()
    cursor.close()

def insert_action_type_to_db(student_number):
    cursor = mysql.connection.cursor()
    query = """
    SELECT sc.result
    FROM answer a
    JOIN statement_choices sc ON a.choice_id = sc.id
    WHERE a.student_number = %s;
    """
    cursor.execute(query, (student_number,))
    results = cursor.fetchall()

    # track amout of occurences of all the letters
    E = 0
    I = 0
    S = 0
    N = 0
    T = 0
    F = 0
    J = 0
    P = 0

    for row in results:
        if row['result'] == 'E':
            E += 1
        elif row['result'] == 'I':
            I += 1
        elif row['result'] == 'S':
            S += 1
        elif row['result'] == 'N':
            N += 1
        elif row['result'] == 'T':
            T += 1
        elif row['result'] == 'F':
            F += 1
        elif row['result'] == 'J':
            J += 1
        elif row['result'] == 'P':
            P += 1
    
    # get the action type
    action_type = ''
    if E > I:
        action_type += 'E'
    else:
        action_type += 'I'
    if S > N:
        action_type += 'S'
    else:
        action_type += 'N'
    if T > F:
        action_type += 'T'
    else:
        action_type += 'F'
    if J > P:
        action_type += 'J'
    else:
        action_type += 'P'

    # add the action type to the database
    cursor.execute('UPDATE students SET action_type = %s WHERE number = %s', (action_type, student_number))
    print(action_type)
    cursor.close()

# get the action type of the student
def get_action_type(student_number):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT action_type FROM students WHERE number = %s', (student_number,))
    result = cursor.fetchall()
    cursor.close()
    if result:
        return result[0]['action_type']
    return False
