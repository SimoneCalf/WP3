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
    print(result)
    return result

