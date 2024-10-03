import mysql.connector

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
    port=config['PORT']
)

mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS wp3")

mycursor.close()
mydb.close()

mydb = mysql.connector.connect(
    host=config['MYSQL_HOST'],
    user=config['MYSQL_USER'],
    password=config['MYSQL_PASSWORD'],
    port=config['PORT'],
    database=config['MYSQL_DB']
)

mycursor = mydb.cursor()

#mycursor.execute("Drop table if exists team;Drop table if exists action_type;Drop table if exists answer;DROP TABLE IF EXISTS students;DROP TABLE IF EXISTS teacher;Drop table if exists statement_number;Drop table if exists teacher;Drop table if exists statement_choices",multi=True)

# Execute multiple statements
mycursor.execute("""
    DROP TABLE IF EXISTS team;
    DROP TABLE IF EXISTS action_type;
    DROP TABLE IF EXISTS answer;
    DROP TABLE IF EXISTS students;
    DROP TABLE IF EXISTS teacher;
    DROP TABLE IF EXISTS statement_number;
    DROP TABLE IF EXISTS statement_choices;
""", multi=True)



mycursor.execute("""
create table statement_choices
(
    id     int auto_increment
        primary key,
    text   varchar(200) not null,
    result varchar(1)   not null
);
"""
)

mycursor.execute("""
create table statement_number
(
    id          int not null AUTO_INCREMENT
        primary key,
    choice_a_id int not null,
    choice_b_id int not null,
    constraint statement_number_statement_choices_id_fk
        foreign key (choice_b_id) references statement_choices (id),
    constraint statement_number_statement_choices_id_fk_2
        foreign key (choice_a_id) references statement_choices (id)
);
"""
)

mycursor.execute("""
create table students
(
    number int          not null
        primary key,
    class  varchar(2)   not null,
    name   varchar(100) not null
);
"""
)

mycursor.execute("""

create table teacher
(
    id        int auto_increment
        primary key,
    name      varchar(100) not null,
    last_name varchar(100) not null,
    email     varchar(255) not null,
    password  varchar(255) not null,
    salt      varchar(255) not null,
    is_admin  tinyint(1)   not null
);
"""
)

mycursor.execute("""                 
create table answer
(
    student_number int not null,
    statement_id    int not null,
    choice_id      int not null,
    primary key (student_number, statement_id),
    constraint answer_statement_number_id_fk
        foreign key (statement_id) references statement_number (id),
    constraint answer_statement_choices_id_fk
        foreign key (choice_id) references statement_choices (id),
    constraint answer_students_number_fk
        foreign key (student_number) references students (number)
);
"""
)

mycursor.execute("""           
CREATE table action_type (
    id INT AUTO_INCREMENT PRIMARY KEY,
    letters VARCHAR(4),
    student_number INT,
    date_assigned DATETIME not null,
    FOREIGN KEY (student_number) REFERENCES students(number)
);
"""
)

mycursor.execute("""                 
CREATE TABLE team (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    student_number INT,
    teacher_id INT,
    FOREIGN KEY (student_number) REFERENCES students(number),
    FOREIGN KEY (teacher_id) REFERENCES teacher(id)
);
                 """)


mycursor.close()
