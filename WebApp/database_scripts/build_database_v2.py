import mysql.connector
from mysql.connector import errorcode

# Assuming config is a dictionary with your database configuration
config = {
    'MYSQL_HOST': 'localhost',
    'MYSQL_USER': 'root',
    'MYSQL_PASSWORD': 'password',
    'PORT': 3306,
    'MYSQL_DB': 'wp3'
}

try:
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

    # Fetch all results to ensure the command is fully processed
    for result in mycursor:
        pass

    # Create table statement_choices
    mycursor.execute("""
        CREATE TABLE statement_choices (
            id INT AUTO_INCREMENT PRIMARY KEY,
            text VARCHAR(200) NOT NULL,
            result VARCHAR(1) NOT NULL
        );
    """)

    mycursor.close()
    mydb.close()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)