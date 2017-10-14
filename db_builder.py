import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


file="eschooldata.db"

db = sqlite3.connect(file) #open if file exists, otherwise create
cursor = db.cursor()       #facilitate db ops

#==========================================================
def SQLcommands(text):
    command = text
    cursor.execute(command)

SQLcommands("CREATE TABLE courses (code TEXT, mark INTEGER, id INTEGER)")
SQLcommands("CREATE TABLE peeps (name TEXT, age INTEGER, id INTEGER)")

with open("data/courses.csv", "rb") as csvfile:
    dictReader = csv.DictReader(csvfile)
    for row in dictReader:
        SQLcommands("INSERT INTO courses VALUES ('" + row["code"] + "', '" + row["mark"] + "', '" + row["id"] + "')")

with open("data/peeps.csv", "rb") as csvfile:
    dictReader = csv.DictReader(csvfile)
    for row in dictReader:
        SQLcommands("INSERT INTO peeps VALUES ('" + row["name"] + "', '" + row["age"] + "', '" + row["id"] + "')")


#==========================================================
db.commit() #save changes
db.close()  #close database
