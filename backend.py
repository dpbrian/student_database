#backend
import sqlite3

datafile = 'student.db'
datadir = 'C:/Users/Brian/Desktop/Python_Projects/student_database_project/'
db = datadir+datafile

 #connects to our database
def StudentData():

    con=sqlite3.connect(db)
    conn.text_factory = sqlite3.OptimizedUnicode
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student (id INTEGER PRIMARY KEY, StdID text, Firstname text, \
        Lastname text, Dob text, \
        Age text, Gender text, Address text, Mobile text)")
    con.commit()
    con.close()

#display our data
def addStdRec(StdID, Firstname, Lastname, Dob, Age, Gender, Address, Mobile):
    con=sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", \
                (StdID, Firstname, Lastname, Dob, Age, Gender, Address, Mobile))
    con.commit()
    con.close()

#View our data
def viewData():
    con=sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows

#View our data
def deleteData(StdID, Firstname, Lastname, Dob, Age, Gender, Address, Mobile):
    con=sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close()

#Search for data
def searchData(StdID="", Firstname="", Lastname="", Dob="", Age="", Gender="", Address="", Mobile=""):
    con=sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID=? OR Firstname=? OR Lastname=? OR Dob=? OR Age=? OR Gender=? OR Address=? OR Mobile=? ", (StdID, Firstname, Lastname, Dob, Age, Gender, Address, Mobile))
    rows = cur.fetchall()
    con.close()
    return rows


#Update data
def updateData(StdID="", Firstname="", Lastname="", Dob="", Age="", Gender="", Address="", Mobile=""):
    con=sqlite3.connect(db)
    cur = con.cursor()
    cur.execute("UPDATE student SET StdID=?, Firstname=?, Lastname=?, Dob=?, Age=?, Gender=?, Address=?, Mobile=?, WHERE id=?", (StdID, Firstname, Lastname, Dob, Age, Gender, Address, Mobile, id))
    rows = cur.fetchall()
    con.commit()
    con.close()
    

    