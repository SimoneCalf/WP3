from flask_mysqldb import MySQL


mysql = MySQL()

# query to get all the teacher information
def get_teacher_info():
    cursor = mysql.connection.cursor()
    cursor.execute('SELECT * FROM teachers')
    result = cursor.fetchall()
    #print(result)
    cursor.close()
    return result