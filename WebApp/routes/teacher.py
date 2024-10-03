from flask import Flask, Blueprint, render_template, request, redirect, url_for, jsonify, session, flash
from flask_login import UserMixin, login_user, login_required
from extensions import login_manager  # Importeer login_manager vanuit extensions.py
# import sql
from models import sql
import hashlib
from database_scripts.hash_and_salt import update_password_hashed_salted


app = Flask(__name__)
teacher_bp = Blueprint('teacher', __name__)



# User class
class User(UserMixin):
    def __init__(self, email):
        self.id = email
        self.email = email

# load the user with the help of the LoginManager
@login_manager.user_loader
def load_user(email):
    if sql.teacher_exists(email):
        # Return a User object if the user exists
        return User(email)
    return None
    

# get students by class and/or team
@teacher_bp.route('/get_students_by_class_and_or_team', methods=['POST', 'GET'])
def get_students_by_class_and_or_team():
    data = request.get_json()
    
    # get the class and team name from the JSON
    student_class = data.get('class_name')
    team_name = data.get('team_name')

    # no class selected, but team selected
    if not student_class and team_name:
        students = sql.get_students_assigned_to_team(team_name)
        return jsonify(students)
    
    # selected class, but no team
    if student_class and not team_name:
        students = sql.get_students_by_class(student_class)
        return jsonify(students)
    
    # no class and no team selected
    if not student_class and not team_name:
        print('Geen klas en geen team geselecteerd')
        students = sql.get_student_info()
        print(f'Students: {students}')
        return jsonify(students)
    
    # selected class and team
    if student_class and team_name:
        print('Zowel klas als team geselecteerd')
        students = sql.get_students_by_class_and_team(student_class, team_name)
        print(f'Students: {students}')
        return jsonify(students)

# get the students wich are assigned to the selected team
@teacher_bp.route('/get_students_by_team', methods=['POST', 'GET'])
def get_students_by_team():
    print('get_students_assigned_to_team')
    data = request.get_json()
    # get the team name from the JSON
    team_name = data.get('team_name')
    # get the students assigned to the selected team
    students = sql.get_students_assigned_to_team(team_name)
    return jsonify(students)

# get the students that are in the selected class
@teacher_bp.route('/get_students_by_class', methods=['POST', 'GET'])
def get_students_by_class():
    data = request.get_json()
    # Haal de gegevens uit de JSON
    student_class = data.get('class_name')
    # get the students that are in the selected class
    students = sql.get_students_by_class(student_class)
    return jsonify(students)

# update information about the student
@teacher_bp.route('/update_student_info', methods=['POST', 'GET'])
def update_student_info():
    data = request.get_json()
    # Haal de gegevens uit de JSON
    # get the name, student number, class and team name from the JSON
    name = data.get('name')
    student_number = data.get('student_number')
    student_class = data.get('student_class')
    team_name = data.get('team_name')
    # get the email of the teacher from the session
    email_teacher = session.get('email_teacher')
    if team_name != 'No Team':
        teacher_id = sql.get_teacher_id(email_teacher)
        sql.add_team_to_student(student_number, team_name, teacher_id)
        
    # process the data
    sql.update_student_info(name, student_number, student_class)
    
    # after successful update, return success response
    return jsonify({'success': True})
 

# This route is used to delete a student from the database
@teacher_bp.route('/delete_student/<int:student_number>', methods=['DELETE'])
def delete_student(student_number):
    # delete the student with the given student number
    success = sql.delete_student(student_number)
    if success:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False}), 500

# This route is used to add new students to the database
@teacher_bp.route('/add_student', methods=['POST'])
def add_student():
    data = request.get_json()
    # get the name, student number and class from the JSON
    name = data.get('name')
    student_number = data.get('student_number')
    student_class = data.get('student_class')
    # process the data
    sql.add_student(name, student_number, student_class)
    
    # after successful addition, return success response
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
    # Retrieve a list of all teams
    team_data = sql.get_teams()
    team_names = []
    for team in team_data:
        team_names.append(team['name'])
    return jsonify(team_data)

# This route is used to delete a teacher from the database. This can be done by teacher who are admin
@teacher_bp.route('/delete_teacher/<int:teacher_id>', methods=['DELETE'])
def delete_teacher(teacher_id):
    # delete the teacher with the given teacher id
    success = sql.delete_teacher(teacher_id)
    if success:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False}), 500

@teacher_bp.route('/add_teacher', methods=['POST'])
def add_teacher():
    data = request.get_json()
    # get the name, lastname, email, password and isAdmin from the JSON
    name = data.get('name')
    lastname = data.get('lastname')
    email = data.get('email')
    password = data.get('password')
    is_admin = data.get('isAdmin')

    # process the data
    sql.add_teacher(name, lastname, email, password, is_admin)
    
    # after successful addition, return success response
    return jsonify({'success': True})

@teacher_bp.route('/teachers_list', methods=['GET'])
def teachers_list():
    # Retrieve a list of all teachers
    teacher_data = sql.get_teacher_info()
    return jsonify(teacher_data)

# Get studentnumbers, names, classes, date the student filled in all questions, action type and the team of all students
@teacher_bp.route('/get_student_info', methods=['GET'])
def get_student_info():
    student_info = sql.get_student_info()
    return jsonify(student_info)

# route to go to the detail page of a student
@teacher_bp.route('/student_detail/<int:student_number>', methods=['GET'])
def student_detail(student_number):
    return render_template('student_detail.html', student_number=student_number)

# route to get the statements the student chose
@teacher_bp.route('/get_student_choices/<int:student_number>', methods=['GET'])
def get_student_choices(student_number):
    # get the statements the student chose
    statements = sql.get_student_choices(student_number)
    return jsonify(statements)

# route to get the name, studentnumber, class, action type, date the student filled in all questions and the team of a student
@teacher_bp.route('/get_student_info_specific_student/<int:student_number>', methods=['GET'])
def get_student_info_specific_student(student_number):
    # get the student info of the specific student
    student_info = sql.get_student_info_specific_student(student_number)
    return jsonify(student_info)


@teacher_bp.route('/', methods=['GET', 'POST'])
def teacher_home():
    if request.method == 'GET':
        return render_template('teacher.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        password = update_password_hashed_salted(password)
        print(f'filled in password: {password}')
        # Hash the password
        login_check = sql.teacher_login(email, password)
        if login_check == True:
            # Make the user and log in
            user = User(email)
            # Put the user in the session
            login_user(user)
            # Save the email in the session
            session['email_teacher'] = email
            # Check if the user is an admin
            admin_check = sql.is_admin(email)
            if admin_check == True:
                return redirect(url_for('teacher.admin_teachers'))
            else:
                return redirect(url_for('teacher.manage_students'))
        else:
            flash('Invalid credentials')
            return render_template('teacher.html')
                
               
@teacher_bp.route('/admin_teachers')
@login_required
def admin_teachers():
    return render_template('admin_teachers.html')

@teacher_bp.route('/manage_students')
@login_required
def manage_students():
    return render_template('manage_students.html')

@teacher_bp.route('/manage_teachers')
@login_required
def manage_teachers():
    return render_template('manage_teachers.html')