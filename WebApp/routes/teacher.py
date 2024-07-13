from flask import Flask, Blueprint, render_template

app = Flask(__name__)
teacher_bp = Blueprint('teacher', __name__)

@teacher_bp.route('/')
def student_home():
    return render_template('teacher.html')