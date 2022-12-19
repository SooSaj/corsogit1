
from MyConnection import MyConnection as Mycon
import mysql.connector


class Query:
    
    def __init__(self):
     self.query =''
     self.connessione1=Mycon()
    
    
    
    def all_film(self):
     try:
        all_films = "SELECT title FROM Film"
        results = self.connessione1.execute(all_films)
        for result in results:
         print(result)

     except mysql.connector.Error as errore:
        print("Si è verificato un errore")
        print(errore)
     
        
    def all_actor(self):
     try:
        all_actors = "SELECT first_name,last_name FROM actor"
        results = self.connessione1.execute(all_actors)
        for result in results:
          print(result)

     except mysql.connector.Error as errore:
        print("Si è verificato un errore") 
        print(errore)
     
        


