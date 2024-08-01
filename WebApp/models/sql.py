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
    query = 'SELECT * FROM choices WHERE statement_number = %s'
    cursor.execute(query, (statement_number,))
    result = cursor.fetchall()
    first_choice = result[0]
    second_choice = result[1]
    cursor.close()
    return first_choice, second_choice