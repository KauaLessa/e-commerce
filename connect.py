import mysql.connector

def create_connection(my_password = 'password', my_port = '3306', hostName= '127.0.0.1', my_user='root'):
    conn = mysql.connector.connect(
        host=hostName,
        user=my_user, 
        password=my_password,
        port=my_port
    )
    
    return conn
