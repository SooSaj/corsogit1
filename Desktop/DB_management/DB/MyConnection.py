import mysql.connector

class MyConnection:
   connection={"host":"localhost", "user":"root", "passwd": "root", "port": "3306", "database": "sakila"}
    
   def __init__(self):
                self.conn = mysql.connector.connect(**self.connection)
            
   def execute(self, query):
                cursor = self.conn.cursor()
                cursor.execute(query)
                return cursor.fetchall()
            
   def close(self):
                if self.conn is not None:
                    self.conn.close()
            
            
        