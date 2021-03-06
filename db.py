import os
from mysql.connector import (connection)
from mysql.connector import errorcode

config = {
  'host': os.environ['DATABASE_IP'],
  'database': os.environ['DATABASE_NAME'],
  'user': os.environ['DATABASE_USER'],
  'password': os.environ['DATABASE_PASSWORD']
}

try:
  conex = connection.MySQLConnection(**config)

  if conex.is_connected():
    db_Info = conex.get_server_info()
    print("Connected to MySQL Server version ", db_Info)
    cursor = conex.cursor()
    cursor.execute("select database();")
    record = cursor.fetchone()
    print("You're connected to database: ", record)

except conex.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
      print("Username or Password error")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
      print("Database does not exist")
    else:
      print(err)

finally:
  cursor.close()
  conex.close()
