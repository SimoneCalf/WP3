from flask import Flask, render_template
from routes.student import student_bp
from routes.teacher import teacher_bp

app = Flask(__name__)
app.register_blueprint(student_bp, url_prefix='/student')
app.register_blueprint(teacher_bp, url_prefix='/teacher')

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)