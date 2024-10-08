from flask import Flask, Blueprint, render_template, request, redirect, url_for, jsonify, session
from models.sql import *


app = Flask(__name__)


student_bp = Blueprint('student', __name__)



@student_bp.route('/', methods=['GET', 'POST'])
def student_home():
    # get the studentnumber that the user entered
    student_number = None
    form_submitted = False
    student = None
    if request.method == 'POST':
        form_submitted = True
        # Get the student number from the form submission
        try:
            student_number = int(request.form.get('student_number'))
            
        except ValueError:
            return render_template('student.html', student=student, form_submitted=form_submitted)
        
        student = get_student(student_number)
        
        if student is False:
            
            return render_template('student.html', student = student, form_submitted = form_submitted)

        if student:
            
            session['student_number'] = student["number"]
            # get the  left off postion from the database
            
            session['question_number'] = get_current_question_number(session['student_number']) +1
            session['max_question_number'] = get_max_quetsion_number()
            
            return redirect(url_for('student.student_questions'))
    return render_template('student.html', student=student, form_submitted=form_submitted)


@student_bp.route('/questions', methods=['GET'])
def student_questions():
    # When the student already filled in all the questions, redirect to the results page
    if get_question(session['question_number']) is False:
        return render_template('already_finished_question_list.html')
    else:  
        # Get the first and second choice of the first question for the student
        first_choice, second_choice = get_question(session['question_number'])
        choices = {
        "first_choice": first_choice['choice_text'],
        "first_choice_id": first_choice['choice_id'],
        "second_choice": second_choice['choice_text'],
        "second_choice_id": second_choice['choice_id']
        }
        return render_template('questions.html', choices=choices)
    
@student_bp.route('/api/first_question', methods=['GET'])
def first_question():
    # get the name and the class
    student_number = session.get('student_number')
    student = get_student(student_number)
    name = student['name']
    class_student = student['class']
    
    
    first_choice, second_choice = get_question(session['question_number'] - 1)
    choices = {
    "first_choice": first_choice['choice_text'],
    "first_choice_id": first_choice['choice_id'],
    "second_choice": second_choice['choice_text'],
    "second_choice_id": second_choice['choice_id']
    }

    return jsonify({
        'name': name,
        'class': class_student,
        'choices': choices})


@student_bp.route('/api/next_choices', methods=['POST'])
def next_choices():
    # get the chosen option from the student
    choice = request.json.get('choice')
    choice_id = request.json.get('choice_id')
    # Log de keuze en verwerk deze
    
    student_number = session.get('student_number')
    
    add_answer(session.get('student_number'), session.get('question_number') - 1, choice_id)


    # code below is to get the next question

    question_number = session.get('question_number')
    if question_number > session.get('max_question_number'):
        # go to the result page
        insert_action_type_to_db(student_number)
        action_type = get_action_type(student_number)
        return jsonify({"done": True, "action_type": action_type}), 200
    

    try:
        next_first_choice, next_second_choice = get_question(question_number)
    except IndexError:
        # give an error message if no question is found
        return jsonify({"error": "No more questions available."}), 404

    next_choices = {
        "first_choice": next_first_choice['choice_text'],
        "first_choice_id": next_first_choice['choice_id'],
        "second_choice": next_second_choice['choice_text'],
        "second_choice_id": next_second_choice['choice_id']
    }
    session['question_number'] += 1
    return jsonify(next_choices)

@student_bp.route('/results', methods=['GET'])
def results():
    action_type = request.args.get('action_type')
    return render_template('just_finished_question_list.html', action_type=action_type)