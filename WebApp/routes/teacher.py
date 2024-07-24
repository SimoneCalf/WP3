from flask import Flask, Blueprint, render_template, request, jsonify
import models.sql

app = Flask(__name__)
teacher_bp = Blueprint('teacher', __name__)

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
        teacher_data = models.sql.get_teacher_info()
        email = request.form.get('email')
        password = request.form.get('password')

        # check if the combination of email and password exists in the database
        for teacher in teacher_data:
            if email == teacher["e-mailadres"] and password == teacher["password"]:
                print(f'Logged in as {teacher["name"]}')
                return render_template('admin_teachers.html')
        return render_template('teacher.html')

@teacher_bp.route('/admin_teachers')
def admin_teachers():
    return render_template('admin_teachers.html')

@teacher_bp.route('/manage_students')
def manage_students():
    return render_template('manage_students.html')

@teacher_bp.route('/manage_teachers')
def manage_teachers():
    return render_template('manage_teachers.html')