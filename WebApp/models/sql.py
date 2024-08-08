from flask_mysqldb import MySQL
import json
from flask import jsonify


mysql = MySQL()

# query to get all the teacher information
def get_teacher_info():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM teachers')
    result = cursor.fetchall()
    cursor.close()
    return result

# query to get all the student information
def get_student_info():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM students')
    result = cursor.fetchall()
    cursor.close()
    #print(f'info about students: {result}')
    return result

def get_max_quetsion_number():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT MAX(id) FROM statement_number')
    result = cursor.fetchall()
    cursor.close()
    if result[0]['MAX(id)'] is None:
        return 0
    return result[0]['MAX(id)']

def get_current_question_number(student_number):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT MAX(statement_id) FROM answer WHERE student_number = %s', (student_number,))
    result = cursor.fetchall()
    cursor.close()
    if result[0]['MAX(statement_id)'] is None:
        return 1
    return result[0]['MAX(statement_id)']

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
    print(f'info about choices: {result}')
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
    print(f'dit is het resultaat: {result}')
    if not result:
        print('no result')
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

# get the question


# # get the choice result (letter that belongs to the choice)
# def get_choice_result(choice_text):
#     cursor = mysql.connection.cursor()
#     query = 'SELECT choice_result FROM choices WHERE choice_text = %s'
#     cursor.execute(query, (choice_text,))
#     result = cursor.fetchall()
#     result = result[0]['choice_result']
#     cursor.close()
#     print(f'choice result: {result}')
#     return result

# add the choice result for the statement number to the database for the student that is logged in
def add_answer(student_number, statement_id, choice_id):
    cursor = mysql.connection.cursor()
    query = 'INSERT INTO answer (student_number, statement_id, choice_id) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE choice_id = %s'
    cursor.execute(query, (student_number, statement_id, choice_id, choice_id,))
    mysql.connection.commit()
    cursor.close()

def get_action_type():
    pass

