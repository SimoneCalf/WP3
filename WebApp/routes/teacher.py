from flask import Flask, Blueprint, render_template, request, jsonify
import models.sql
# import sql
from models import sql

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
        email = request.form.get('email')
        password = request.form.get('password')
        print(f'Email: {email}')
        print(f'Password: {password}')
        login_check = sql.teacher_login(email, password)
        print(f'Login check: {login_check}')
        if login_check == True:
            # check if the teacher is an admin
            admin_check = sql.is_admin(email)
            print(f'Admin check: {admin_check}')
            if admin_check == True:
                return render_template('admin_teachers.html')
            else:
                return render_template('manage_students.html')
        

@teacher_bp.route('/admin_teachers')
def admin_teachers():
    return render_template('admin_teachers.html')

@teacher_bp.route('/manage_students')
def manage_students():
    return render_template('manage_students.html')

@teacher_bp.route('/manage_teachers')
def manage_teachers():
    return render_template('manage_teachers.html')