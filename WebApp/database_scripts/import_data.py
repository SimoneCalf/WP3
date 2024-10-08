import mysql.connector
import json
from hash_and_salt import update_password_hashed_salted

# MySQL configuration
config = {}
config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/wp3'
config['MYSQL_HOST'] = 'localhost'
config['MYSQL_USER'] = 'root'
config['MYSQL_PASSWORD'] = 'actiontypes_wp3'
config['MYSQL_DB'] = 'wp3'
config['MYSQL_CURSORCLASS'] = 'DictCursor'
config['PORT'] = 3307


mydb = mysql.connector.connect(
    host=config['MYSQL_HOST'],
    user=config['MYSQL_USER'],
    password=config['MYSQL_PASSWORD'],
    port=config['PORT'],
    database=config['MYSQL_DB']
)


def drop_all_data():
    mycursor = mydb.cursor()
    try:
        mycursor.execute("DELETE FROM team")
        mycursor.execute("DELETE FROM teacher")
        mycursor.execute("DELETE FROM answer")
        mycursor.execute("DELETE FROM students")
        mycursor.execute("DELETE FROM statement_number")
        mycursor.execute("DELETE FROM statement_choices")

        # Reset auto-increment
        mycursor.execute("ALTER TABLE team AUTO_INCREMENT = 1")
        mycursor.execute("ALTER TABLE teacher AUTO_INCREMENT = 1")
        mycursor.execute("ALTER TABLE answer AUTO_INCREMENT = 1")
        mycursor.execute("ALTER TABLE students AUTO_INCREMENT = 1")
        mycursor.execute("ALTER TABLE statement_number AUTO_INCREMENT = 1")
        mycursor.execute("ALTER TABLE statement_choices AUTO_INCREMENT = 1")
    finally:
        mycursor.close()

## TEACHERS
def teachers():
    mycursor = mydb.cursor()
    hashed_passwords = []
    try:
        with open("../json/teachers.json") as file:
            data = json.load(file)

        # hash passwords
        for teacher in data:
            # add salt and hashed password to the database
            print(f'teacher passwords from json: {teacher["password"]}')
            hashed_passwords, salt = update_password_hashed_salted(teacher['password'])
            salt = salt
            password = hashed_passwords
            mycursor.execute("INSERT INTO teacher (name, last_name, email, password, salt, is_admin) VALUES (%s, %s, %s, %s, %s, %s)",
                            (teacher['name'], teacher['last_name'], teacher['email'], password, salt, teacher['is_admin']))
    finally:
        mycursor.close()

## STUDENTS
def students():
    mycursor = mydb.cursor()
    try:
        with open("../json/students.json") as file:
            data = json.load(file)

        for student in data:
            mycursor.execute("INSERT INTO students (class, name, number) VALUES (%s, %s, %s)",
                            (student['student_class'], student['student_name'], student['student_number']))
    finally:
        mycursor.close()

## TEAMS
def teams():
    mycursor = mydb.cursor()
    try:
        with open("./json/students.json") as file:
            data = json.load(file)

        for student in data:
            mycursor.execute("INSERT INTO team (student_number) VALUES (%s)",
                            (student['student_number'],))
    finally:
        mycursor.close()

## STATEMENTS
def statements():
    mycursor = mydb.cursor()
    try:
        with open("../json/actiontype_statements.json") as file:
            data = json.load(file)

        for statement in data:
            choices_ids = []
            for choice in statement['statement_choices']:
                ## Insert but save ID
                mycursor.execute("INSERT INTO statement_choices (text, result) VALUES (%s, %s)",
                                (choice['choice_text'], choice['choice_result']))
                choices_ids.append(mycursor.lastrowid)


            mycursor.execute("INSERT INTO statement_number (choice_a_id, choice_b_id) VALUES (%s, %s)",
                            (choices_ids[0], choices_ids[1]))
    finally:
        mycursor.close()


drop_all_data()
teachers()
students()
statements()
mydb.commit()
mydb.close()