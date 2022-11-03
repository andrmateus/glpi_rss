import mysql.connector as mysql
import os

class connectDB:
    def __init__(self):
        print('class connect')
        
        self.myconnect = mysql.connect(
            user = os.getenv('MYSQL_USER'),
            host = os.getenv('MYSQL_HOST'),
            password = os.getenv('MYSQL_PASSWORD'),
            db = 'glpi'
        )