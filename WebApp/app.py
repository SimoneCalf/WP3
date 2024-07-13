from flask import Flask, render_template
from routes.student import student_bp

app = Flask(__name__)
app.register_blueprint(student_bp, url_prefix='/student')

@app.route('/')
def home():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)