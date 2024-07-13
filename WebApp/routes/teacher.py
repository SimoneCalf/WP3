from flask import Flask, Blueprint, render_template

app = Flask(__name__)
teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/')
def teacher_home():
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