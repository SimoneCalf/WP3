from flask import Flask, Blueprint, render_template, request, redirect, url_for, jsonify, session, flash
import models.sql
# import sql
from models import sql
import sys

app = Flask(__name__)
teacher_bp = Blueprint('teacher', __name__)

# get students by class and/or team
@teacher_bp.route('/get_students_by_class_and_or_team', methods=['POST', 'GET'])
def get_students_by_class_and_or_team():
    data = request.get_json()
    
    # Haal de gegevens uit de JSON
    student_class = data.get('class_name')
    team_name = data.get('team_name')
    print(f'Student class: {student_class}, team name: {team_name}')

    # geen klas geselecteerd, maar wel team
    if not student_class and team_name:
        print('Geen klas geselecteerd, maar wel team')
        students = sql.get_students_assigned_to_team(team_name)
        print(f'Students: {students}')
        return jsonify(students)
    
    # wel klas geselecteerd, maar geen team
    if student_class and not team_name:
        print('Wel klas geselecteerd maar geen team')
        students = sql.get_students_by_class(student_class)
        print(f'Students: {students}')
        return jsonify(students)
    
    # geen klas en geen team geselecteerd
    if not student_class and not team_name:
        print('Geen klas en geen team geselecteerd')
        students = sql.get_student_info()
        print(f'Students: {students}')
        return jsonify(students)
    
    # zowel klas als team geselecteerd
    if student_class and team_name:
        print('Zowel klas als team geselecteerd')
        students = sql.get_students_by_class_and_team(student_class, team_name)
        print(f'Students: {students}')
        return jsonify(students)




    # # get the students by class and/or team
    # students = sql.get_students_by_class_and_or_team(student_class, team_name)
    # print(f'Students: {students}')
    # return jsonify(students)


# get the students wich are assigned to the selected team
@teacher_bp.route('/get_students_by_team', methods=['POST', 'GET'])
def get_students_by_team():
    print('get_students_assigned_to_team')
    data = request.get_json()
    print(f'Received data: {data}')
    # Haal de gegevens uit de JSON
    team_name = data.get('team_name')
    print(f'Team name: {team_name}')
    # get the students assigned to the selected team
    students = sql.get_students_assigned_to_team(team_name)
    print(f'Students: {students}')
    return jsonify(students)

# get the students that are in the selected class
@teacher_bp.route('/get_students_by_class', methods=['POST', 'GET'])
def get_students_by_class():
    print('get_students_by_class')
    data = request.get_json()
    print(f'Received data: {data}')
    # Haal de gegevens uit de JSON
    student_class = data.get('class_name')
    print(f'Student class: {student_class}')
    # get the students that are in the selected class
    students = sql.get_students_by_class(student_class)
    print(f'Students: {students}')
    return jsonify(students)

# update information about the student
@teacher_bp.route('/update_student_info', methods=['POST', 'GET'])
def update_student_info():
    print('update_student_info')
    data = request.get_json()
    print(f'Received data: {data}')
    # Haal de gegevens uit de JSON
    name = data.get('name')
    student_number = data.get('student_number')
    student_class = data.get('student_class')
    team_name = data.get('team_name')
    email_teacher = session.get('email_teacher')
    if team_name != 'No Team':
        print(f'Session: {session}')
        print(f'teacher_email: {email_teacher}')
        teacher_id = sql.get_teacher_id(email_teacher)
        print(f'teacher_id: {teacher_id}')
        sql.add_team_to_student(student_number, team_name, teacher_id)
        
    #print(f'Name: {name}, student number: {student_number}, student class: {student_class}')
    #print(type(student_number))
    # Verwerk de gegevens (bijvoorbeeld opslaan in een database)
    sql.update_student_info(name, student_number, student_class)
    
    # Na succesvolle toevoeging, retourneer succesresponse
    return jsonify({'success': True})
 

# This route is used to delete a student from the database
@teacher_bp.route('/delete_student/<int:student_number>', methods=['DELETE'])
def delete_student(student_number):
    # Verwijder de student met het opgegeven studentnummer
    success = sql.delete_student(student_number)
    if success:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False}), 500

# This route is used to add new students to the database
@teacher_bp.route('/add_student', methods=['POST'])
def add_student():
    data = request.get_json()
    #print(f'Received data: {data}')
    # Haal de gegevens uit de JSON
    name = data.get('name')
    student_number = data.get('student_number')
    student_class = data.get('student_class')
    #print(f'Name: {name}, student number: {student_number}, student class: {student_class}')
    #print(type(student_number))
    # Verwerk de gegevens (bijvoorbeeld opslaan in een database)
    sql.add_student(name, student_number, student_class)
    
    # Na succesvolle toevoeging, retourneer succesresponse
    return jsonify({'success': True})

# This route is used to get all the classes that are in the database
@teacher_bp.route('/get_classes', methods=['GET'])
def get_classes():
    # Retrieve a list of all classes
    class_data = sql.get_classes()
    return jsonify(class_data)

# This route is used to add all existing teams to a dropdown menu
@teacher_bp.route('/get_teams', methods=['GET'])
def get_teams():
    print('gelut om naar de url te gaan')
    # Retrieve a list of all teams
    team_data = sql.get_teams()
    print(f'Team data: {team_data}')
    team_names = []
    for team in team_data:
        team_names.append(team['name'])
    print(f'Team names: {team_names}')
    return jsonify(team_data)

# This route is used to delete a teacher from the database. This can be done by teacher who are admin
@teacher_bp.route('/delete_teacher/<int:teacher_id>', methods=['DELETE'])
def delete_teacher(teacher_id):
    print('hallo')
    # Verwijder de docent met het opgegeven ID
    success = sql.delete_teacher(teacher_id)
    if success:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False}), 500

@teacher_bp.route('/add_teacher', methods=['POST'])
def add_teacher():
    data = request.get_json()

    # Haal de gegevens uit de JSON
    name = data.get('name')
    lastname = data.get('lastname')
    email = data.get('email')
    password = data.get('password')
    is_admin = data.get('isAdmin')

    # Verwerk de gegevens (bijvoorbeeld opslaan in een database)
    sql.add_teacher(name, lastname, email, password, is_admin)
    
    # Na succesvolle toevoeging, retourneer succesresponse
    return jsonify({'success': True})

@teacher_bp.route('/teachers_list', methods=['GET'])
def teachers_list():
    # Retrieve a list of all teachers
    teacher_data = sql.get_teacher_info()
    return jsonify(teacher_data)

# Get studentnumbers, names, classes, date the student filled in all questions, action type and the team of all students
@teacher_bp.route('/get_student_info', methods=['GET'])
def get_student_info():
    #print('hallo')
    student_info = sql.get_student_info()
    #print(f'Student info: {student_info}')
    return jsonify(student_info)

# route to go to the detail page of a student
@teacher_bp.route('/student_detail/<int:student_number>', methods=['GET'])
def student_detail(student_number):
    print(f'Student number: {student_number}')
    # get the statements the student chose
    # statements = sql.get_student_choices(student_number)
    # print(f'Statements: {statements}')
    return render_template('student_detail.html', student_number=student_number)

# route to get the statements the student chose
@teacher_bp.route('/get_student_choices/<int:student_number>', methods=['GET'])
def get_student_choices(student_number):
    #print(f'Student number: {student_number}')
    # get the statements the student chose
    statements = sql.get_student_choices(student_number)
    #print(f'Statements: {statements}')
    return jsonify(statements)

# route to get the name, studentnumber, class, action type, date the student filled in all questions and the team of a student
@teacher_bp.route('/get_student_info_specific_student/<int:student_number>', methods=['GET'])
def get_student_info_specific_student(student_number):
    #print(f'Student number: {student_number}')
    # get the student info of the specific student
    student_info = sql.get_student_info_specific_student(student_number)
    #print(f'Student info: {student_info}')
    return jsonify(student_info)


# @teacher_bp.route('/login', methods=['POST'])
# def teacher_login():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')
#     print(f'Received email: {email}, password: {password}')  # Log de ontvangen data
#     return jsonify({'success': True})

@teacher_bp.route('/', methods=['GET', 'POST'])
def teacher_home():
    if request.method == 'GET':
        return render_template('teacher.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        #print(f'Email: {email}')
        #print(f'Password: {password}')
        login_check = sql.teacher_login(email, password)
        #print(f'Login check: {login_check}')
        if login_check == True:
            # add teacher to the session
            session['email_teacher'] = email
            print(f'Session: {session}')
            email_teacher = session.get('email_teacher')
            print(f'Email teacher: {email_teacher}')
            # check if the teacher is an admin
            admin_check = sql.is_admin(email)
            #print(f'Admin check: {admin_check}')
            if admin_check == True:
                return redirect(url_for('teacher.admin_teachers'))
            else:
                
                return redirect(url_for('teacher.manage_students'))
                # redirect to admin_teahers route
        else:
            return render_template('teacher.html')
                
                
        

@teacher_bp.route('/admin_teachers')
def admin_teachers():
    return render_template('admin_teachers.html')

@teacher_bp.route('/manage_students')
def manage_students():
    return render_template('manage_students.html')

@teacher_bp.route('/manage_teachers')
def manage_teachers():
    # retrieve a list of al the teachers
    teacher_data = sql.get_teacher_info()
    #print(f'Teacher data: {teacher_data}')
    return render_template('manage_teachers.html')