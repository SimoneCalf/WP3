from flask import Flask, Blueprint, render_template

app = Flask(__name__)
student_bp = Blueprint('student', __name__)

@student_bp.route('/')
def student_home():
    return render_template('student.html')