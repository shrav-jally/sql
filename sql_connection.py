import datetime
import mysql.connector

__cnx = None  #if we call this funciton multiple times, we want to reuse the connection under this global variable

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:  #if this connection is not already opened, then only we open it
    __cnx = mysql.connector.connect(user='root', password='root', database='gs')

  return __cnx
