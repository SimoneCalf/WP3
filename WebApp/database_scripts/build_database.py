import mysql.connector
import json

# MySQL configuration
config = {}
config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:admin@localhost/wp3'
config['MYSQL_HOST'] = 'localhost'
config['MYSQL_USER'] = 'root'
config['MYSQL_PASSWORD'] = 'admin'
config['MYSQL_DB'] = 'wp3'
config['MYSQL_CURSORCLASS'] = 'DictCursor'

mydb = mysql.connector.connect(
    host=config['MYSQL_HOST'],
    user=config['MYSQL_USER'],
    password=config['MYSQL_PASSWORD'],
    database=config['MYSQL_DB']
)

mycursor = mydb.cursor()

mycursor.execute("Drop table if exists answer;DROP TABLE IF EXISTS students;DROP TABLE IF EXISTS teacher;Drop table if exists statement_number;Drop table if exists teacher;Drop table if exists statement_choices;",multi=True)


mycursor.execute("""
                 
create table statement_choices
(
    id     int auto_increment
        primary key,
    text   varchar(200) not null,
    result varchar(1)   not null
);

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

create table students
(
    number int          not null
        primary key,
    class  varchar(2)   not null,
    name   varchar(100) not null
);

create table teacher
(
    id        int auto_increment
        primary key,
    name      varchar(100) not null,
    last_name varchar(100) not null,
    email     varchar(255) not null,
    password  varchar(255) not null,
    is_admin  tinyint(1)   not null
);
                 
create table answer
(
    student_number int not null,
    statment_id    int not null,
    choice_id      int not null,
    primary key (student_number, statment_id),
    constraint answer_statement_number_id_fk
        foreign key (statment_id) references statement_number (id),
    constraint answer_statement_choices_id_fk
        foreign key (choice_id) references statement_choices (id),
    constraint answer_students_number_fk
        foreign key (student_number) references students (number)
);

                 """, multi=True)
