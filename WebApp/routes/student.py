from flask import Flask, Blueprint, render_template, request, redirect, url_for
from models.sql import *


app = Flask(__name__)
student_bp = Blueprint('student', __name__)



@student_bp.route('/', methods=['GET', 'POST'])
def student_home():
    # get the studentnumber that the user entered
    student_number = None
    if request.method == 'POST':
        # Get the student number from the form submission
        try:
            student_number = int(request.form.get('student_number'))
            print(f'student number: {student_number}')
        except ValueError:
            return render_template('student.html')
        student_info = get_student_info()
        # check if the student number is in the database
        for student in student_info:
            number_from_db = int(student['student_number'])
            if student_number == number_from_db:
                return redirect(url_for('student.student_questions'))
    return render_template('student.html')

@student_bp.route('/questions', methods=['GET', 'POST'])
def student_questions():
    first_choice, second_choice = get_first_question(1)
    first_choice = first_choice['choice_text']
    second_choice = second_choice['choice_text']
    if request.method == 'POST':
        print('post request')
        # get the choice that the student made
        choice = request.form.get('choice')
        # get the second question
        first_choice = ""
        second_choice = ""
        print(f'choice: {choice}')
    return render_template('questions.html', first_choice=first_choice, second_choice=second_choice)

# route that returns the questions in JSON-format
@student_bp.route('/api/questions', methods=['GET', 'POST'])
def get_questions():
    if request.method == 'GET':
        first_choice, second_choice = get_first_question(1)
        questions = {
            "first_choice": first_choice['choice_text'],
            "second_choice": second_choice['choice_text']
        }
        return jsonify(questions)
    if request.method == 'POST':
        # get the choice that the student made
        choice = request.form.get('choice')
        # get the second question
        first_choice = ""
        second_choice = ""
        print(f'choice: {choice}')