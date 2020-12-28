import sqlite3

class Person:
    def __init__(self,id_number=-1, first="", last="", age=-1):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect("ChelseaPlayers.db")
        self.cursor = self.connection.cursor()

    
    def load_person(self, id_number):

        self.cursor.execute("SELECT * FROM PLAYERS WHERE id = {}".format(id_number))
        results = self.cursor.fetchone()
        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]

    def insert_person(self):
        self.cursor.execute("INSERT INTO PLAYERS VALUES ({}, '{}', '{}', {})".format(self.id_number,self.first,self.last,self.age))

        self.connection.commit()
        self.connection.close()
""" 
connection = sqlite3.connect('ChelseaPlayers.db')
cursor = connection.cursor()



cursor.execute(" CREATE TABLE IF NOT EXISTS PLAYERS (id INTEGER PRIMARY KEY, First_name VARCHAR32, LAST_Name VARCHAR32, AGE INTEGER )")
cursor.execute("INSERT INTO PLAYERS VALUES (1,'Ngolo','Kante',29),(2,'Oliver','Giroud',34),(3,'Christian','Pulisic',22)")

cursor.execute(("SELECT * FROM PLAYERS WHERE Last_Name = 'Giroud' "))
rows = cursor.fetchall()
print(rows)
connection.commit()
connection.close() """

p2=Person(5,"Cesar","Aspillicueta",29)
p2.insert_person()
connection = sqlite3.connect("ChelseaPlayers.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM PLAYERS")
results = cursor.fetchall()
print(results)

connection.close()