import pymysql as MySQLdb

HOST = 'localhost'
USER = 'root'
PASSWORD = 'toor'
DATABASE = 'minicurso_python'

USER_TABLE = """CREATE TABLE users(
                id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
                username VARCHAR(50) NOT NULL,
                password VARCHAR(50) NOT NULL
                )"""

DROP_USER = "DROP TABLE IF EXISTS `users`"
SHOW_TABLES = "SHOW TABLES"

if __name__ == '__main__':
    try:
        connection = MySQLdb.connect(HOST, USER, PASSWORD, DATABASE)

        cursor = connection.cursor()
        
        cursor.execute(DROP_USER)
        cursor.execute(USER_TABLE)

        cursor.execute(SHOW_TABLES)
        tables = cursor.fetchall()

        for table in tables:
            print(table[0])

        connection.close()
    
    except MySQLdb.Error as error:
        print(error)
