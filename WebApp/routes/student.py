from flask import Flask, Blueprint, render_template, request, redirect, url_for, jsonify, session
import secrets
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
                # if the student number is in the database, create a session for the student
                session['student_number'] = student_number
                session['question_number'] = 1
                print("Current session data:", dict(session))
                return redirect(url_for('student.student_questions'))
    return render_template('student.html')


@student_bp.route('/questions', methods=['GET'])
def student_questions():
    first_choice, second_choice = get_question(1)
    choices = {
    "first_choice": first_choice['choice_text'],
    "second_choice": second_choice['choice_text']
    }
    return render_template('questions.html', choices=choices)
    
@student_bp.route('/api/first_question', methods=['GET'])
def first_question():
    first_choice, second_choice = get_question(1)
    choices = {
    "first_choice": first_choice['choice_text'],
    "second_choice": second_choice['choice_text']
    }
    session['question_number'] += 1
    return jsonify(choices)


@student_bp.route('/api/next_choices', methods=['POST'])
def next_choices():

    # code below is to add the choice result to the database
    
    # Determine the statement number
    statement_number = session.get('question_number')
    statement_number -= 1
    print(f'dit is de statement_number: {statement_number}')

    # Determine the student number
    student_number = session.get('student_number')
    print(f'dit is de student_number: {student_number}')

    # Get the choice result of the statement that the student chose
    data = request.get_json()
    print(f'dit is de data: {data}')
    chosen_option = data.get('choice')
    print(f'dit is de chosen_option: {chosen_option}')
    choice_result = get_choice_result(chosen_option)

    

   
    # code below is to get the next question

    question_number = session.get('question_number')

    try:
        next_first_choice, next_second_choice = get_question(question_number)
    except IndexError:
        # Geef een foutmelding terug als er geen vraag wordt gevonden
        return jsonify({"error": "No more questions available."}), 404

    next_choices = {
        "first_choice": next_first_choice['choice_text'],
        "second_choice": next_second_choice['choice_text']
    }
    session['question_number'] += 1
    return jsonify(next_choices)

   