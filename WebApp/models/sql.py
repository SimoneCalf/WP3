from flask_mysqldb import MySQL
import json
from flask import jsonify
from datetime import datetime

mysql = MySQL()

# # get the name, studentnumber, class, action type, date the student filled in all questions and the team of a student
# def get_student_info_specific_student(student_number):
#     cursor = mysql.connection.cursor()
#     query = '''
#         SELECT
#             s.number AS student_number,
#             s.name AS student_name,
#             s.class AS student_class,
#             COALESCE(at.date_assigned, 'Nog niet ingevuld') AS action_date,
#             COALESCE(at.letters, 'Nog geen') AS action_type,
#             COALESCE(t.name, 'No Team') AS team_name
#         FROM students s
#         LEFT JOIN action_type at ON s.number = at.student_number
#         LEFT JOIN team t ON s.number = t.student_number
#         WHERE s.number = %s;
#     '''
#     cursor.execute(query, (student_number,))
#     result = cursor.fetchall()
#     cursor.close()
#     return result

# get students assigned to a team
def get_students_assigned_to_team(team_name):
    cursor = mysql.connection.cursor()
    query = '''
        SELECT s.number AS student_number, s.name AS student_name, s.class AS student_class,
            IFNULL(a.date_assigned, 'No Data') AS action_date,
            IFNULL(at.letters, 'No Data') AS action_type,
            t.name AS team_name
        FROM students s
        LEFT JOIN action_type a ON s.number = a.student_number
        LEFT JOIN team t ON s.number = t.student_number
        LEFT JOIN action_type at ON s.number = at.student_number
        WHERE t.name = %s
    '''
    cursor.execute(query, (team_name,))
    result = cursor.fetchall()
    cursor.close()
    return result

# get the id of the teacher
def get_teacher_id(email):
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id FROM teacher WHERE email = %s', (email,))
        result = cursor.fetchone()
        
        print(f'result: {result}')
        
        if result and 'id' in result:
                teacher_id = result['id']
                return teacher_id
        else:
            raise ValueError("No teacher found with the provided email.")
    except Exception as e:
        cursor.close()
        cursor.close()

# add team to student
def add_team_to_student(student_number, team_name, teacher_id):
    cursor = mysql.connection.cursor()
    query = '''
    DELETE FROM team WHERE student_number = %s;
    '''
    cursor.execute(query, (student_number,))
    query = '''
        INSERT INTO team (student_number, name, teacher_id)
        VALUES (%s, %s, %s);
    '''
    cursor.execute(query, (student_number, team_name, teacher_id,))
    mysql.connection.commit()
    cursor.close()
   


# update information of a student
def update_student_info(name, number, class_student):
    cursor = mysql.connection.cursor()
    cursor.execute('UPDATE students SET name = %s, class = %s WHERE number = %s', (name, class_student, number,))
    mysql.connection.commit()
    cursor.close()

# function to retrieve all existing teams
def get_teams():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT DISTINCT name FROM team')
    result = cursor.fetchall()
    cursor.close()
    return result

def get_student_info_specific_student(student_number):
    cursor = mysql.connection.cursor()
    query = '''
        SELECT
            s.number AS student_number,
            s.name AS student_name,
            s.class AS student_class,
            COALESCE(at.date_assigned, 'Nog niet ingevuld') AS action_date,
            COALESCE(at.letters, 'Nog geen') AS action_type,
            COALESCE(t.name, 'No Team') AS team_name,
            COALESCE(CONCAT(tch.name, ' ', tch.last_name), 'No Teacher') AS teacher_name
        FROM students s
        LEFT JOIN action_type at ON s.number = at.student_number
        LEFT JOIN team t ON s.number = t.student_number
        LEFT JOIN teacher tch ON t.teacher_id = tch.id
        WHERE s.number = %s;
    '''
    cursor.execute(query, (student_number,))
    result = cursor.fetchall()
    cursor.close()
    #print(f'resultaat 2: {result}')
    return result

# function to delete a student from the database
def delete_student(student_number):
    cursor = mysql.connection.cursor()
    # delete the team
    cursor.execute('DELETE FROM team WHERE student_number = %s', (student_number,))
    # delete the action type
    cursor.execute('DELETE FROM action_type WHERE student_number = %s', (student_number,))
    # delete the answers
    cursor.execute('DELETE FROM answer WHERE student_number = %s', (student_number,))
    cursor.execute('DELETE FROM students WHERE number = %s', (student_number,))
    mysql.connection.commit()
    cursor.close()
    return True


# get the statements a student chose
def get_student_choices(student_number):
    cursor = mysql.connection.cursor()
    query = '''
        SELECT sc.text
        FROM answer a
        JOIN statement_choices sc ON a.choice_id = sc.id
        WHERE a.student_number = %s;
    '''
    cursor.execute(query, (student_number,))
    result = cursor.fetchall()
    cursor.close()
    return result

# # get the statements a student chose
# def get_student_choices(student_number):
#     cursor = mysql.connection.cursor()
#     query = '''
#         SELECT 
#             sn.id AS statement_id,
#             sc_a.text AS choice_a_text,
#             sc_b.text AS choice_b_text,
#             sc_a.result AS choice_a_result,
#             sc_b.result AS choice_b_result
#         FROM 
#             answer a
#         JOIN 
#             statement_number sn ON a.statement_id = sn.id
#         JOIN 
#             statement_choices sc_a ON sn.choice_a_id = sc_a.id
#         JOIN 
#             statement_choices sc_b ON sn.choice_b_id = sc_b.id
#         WHERE 
#             a.student_number = %s;
#     '''
#     cursor.execute(query, (student_number,))
#     result = cursor.fetchall()
#     cursor.close()
#     return result

# get student information
def get_number_class_name():
    cursor = mysql.connection.cursor()
    query = '''
        SELECT
            s.number AS student_number,
            s.name AS student_name,
            s.class AS student_class,
        FROM students s
        ORDER BY s.number;
    '''
    cursor.execute(query)
    result = cursor.fetchall()
    print(f'resultaat 1: {result}')
    cursor.close()
    return result



# get student information
def get_student_info():
    print('get_student_info')
    cursor = mysql.connection.cursor()
    query = '''
        SELECT 
            s.number AS student_number,
            s.name AS student_name,
            s.class AS student_class,
            COALESCE(at.date_assigned, 'No Data') AS action_date,
            COALESCE(at.letters, 'No Data') AS action_type,
            COALESCE(t.name, 'No Team') AS team_name
        FROM students s
        LEFT JOIN action_type at ON s.number = at.student_number
        LEFT JOIN team t ON s.number = t.student_number
        ORDER BY s.number;
    '''
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    #print(result)
    return result

# add a student to the database
def add_student(name, number, class_student):
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO students (name, number, class) VALUES (%s, %s, %s)', (name, number, class_student,))
    mysql.connection.commit()
    cursor.close()

# get all the existing classes
def get_classes():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT DISTINCT class FROM students')
    result = cursor.fetchall()
    cursor.close()
    return result

# delete teacher from the database
def delete_teacher(id):
    cursor = mysql.connection.cursor()
    cursor.execute('DELETE FROM teacher WHERE id = %s', (id,))
    mysql.connection.commit()
    cursor.close()
    return True

# add a teacher to the database
def add_teacher(name, lastname, email, password, is_admin):
    cursor = mysql.connection.cursor()
    cursor.execute('INSERT INTO teacher (name, last_name, email, password, is_admin) VALUES (%s, %s, %s, %s, %s)', (name, lastname, email, password, is_admin,))
    mysql.connection.commit()
    cursor.close()

# determine if the teacher filles in a correct email- and password combination
def teacher_login(email, password):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM teacher WHERE email = %s AND password = %s', (email, password,))
    result = cursor.fetchall()
    cursor.close()
    if result:
        return True
    return False

# determine if the teacher is an admin
def is_admin(email):
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT is_admin FROM teacher WHERE email = %s', (email,))
    result = cursor.fetchall()
    cursor.close()
    if result[0]['is_admin'] == 1:
        return True
    return False

# query to get all the teacher information
def get_teacher_info():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM teacher')
    result = cursor.fetchall()
    cursor.close()
    return result

# # query to get all the student information
# def get_student_info():
#     cursor = mysql.connection.cursor()
#     cursor.execute('SELECT * FROM students')
#     result = cursor.fetchall()
#     cursor.close()
#     return result

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
        print(f'resultaat: {result}')
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
    # get the current datetime
    now = datetime.now()
    # format the date and time
    formatted_date = now.strftime('%Y-%m-%d %H:%M:%S')
    print(f'formatted date: {formatted_date}')
    # add the action type to the database
    cursor.execute('INSERT INTO action_type (letters, student_number, date_assigned) VALUES (%s, %s, %s)', (action_type, student_number, formatted_date))
    print(action_type)
    # commit the changes
    mysql.connection.commit()
    cursor.close()

# get the action type of the student
def get_action_type(student_number):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT letters FROM action_type WHERE student_number = %s", (student_number,))
    result = cursor.fetchone()
    print(f'result: {result}')
    cursor.close()
    if result:
        return result['letters']
    return False
