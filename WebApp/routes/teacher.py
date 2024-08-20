from flask import Flask, Blueprint, render_template, request, jsonify, redirect, url_for
import models.sql
# import sql
from models import sql
import sys

app = Flask(__name__)
teacher_bp = Blueprint('teacher', __name__)

# This route is used to delete a student from the database
@teacher_bp.route('/delete_student/<int:student_number>', methods=['DELETE'])
def delete_student(student_number):
    print('hallo')
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
            # check if the teacher is an admin
            admin_check = sql.is_admin(email)
            #print(f'Admin check: {admin_check}')
            if admin_check == True:
                return redirect(url_for('teacher.admin_teachers'))
            else:
                return redirect(url_for('teacher.manage_students'))
                # redirect to admin_teahers route
                
                
        

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