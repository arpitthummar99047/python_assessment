import mysql.connector

def connect():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mr.at.log91061",
            database="bankdata1",
            port="3306"
        )
      
        return connection
    except mysql.connector.Error as error:
        print("Error connecting to MySQL database:", error)
        return None

