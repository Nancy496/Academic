#!/usr/bin/env python
# coding: utf-8

# In[11]:


pip install mysql-connector-python==8.0.17


# In[53]:


import mysql.connector as conn
mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Academics")


# In[54]:


mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS Academics")
print("Database created")


# In[40]:


mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)


# In[56]:


mycursor.execute("CREATE TABLE College (College_id INT PRIMARY KEY, college_Name VARCHAR(100),college_city VARCHAR(100), college_Country VARCHAR(100))")


# In[ ]:





# In[57]:



mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


# In[12]:


import mysql.connector as conn

mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Academics")

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE IF NOT EXISTS Professor (Teacher_Id INT PRIMARY KEY,Teacher_Name VARCHAR(100),Teacher_Email VARCHAR(100),College_id INT,Date_joined DATE,Speciality VARCHAR(100),Salary DECIMAL(8,2),Experience VARCHAR(100))")
print("Professor table created")


# In[13]:


import mysql.connector as conn

mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Academics")

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE Student (Student_Id INT PRIMARY KEY,Student_Name VARCHAR(100),College_Id INT,Date_joined DATE,Major_taken VARCHAR(100),College_Level VARCHAR(100))")
print("Student table created")


# In[30]:


import mysql.connector as conn
import csv
mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Academics")

mycursor = mydb.cursor()

# Read from csv file
Nancy = csv.reader(open(r"C:\Users\User\Downloads\College.csv",'r'))
next(Nancy) #Skip the first row 
    
    #insert records line by line
for row in Nancy:
    mycursor.execute('INSERT IGNORE INTO College(College_ID,College_Name, College_City,College_Country) VALUES(%s,%s,%s,%s)',row)
mydb.commit() 
print("Records added to college table")


# In[33]:


import mysql.connector as conn
import csv
mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Academics")

mycursor = mydb.cursor()

# Read from csv file
Nancy1 = csv.reader(open(r"C:\Users\User\Downloads\Professor.csv",'r'))
next(Nancy1) #Skip the first row 
    
    #insert records line by line
for row in Nancy1:
    mycursor.execute('INSERT IGNORE INTO Professor( Teacher_ID, Teacher_Name, Teacher_Email, College_ID, Date_Joined, Speciality, Salary, Experience) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)',row)
mydb.commit() 
print("Records added to Professor table")


# In[34]:


import mysql.connector as conn
import csv
mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Academics")

mycursor = mydb.cursor()

# Read from csv file
Nancy2 = csv.reader(open(r"C:\Users\User\Downloads\Student.csv",'r'))
next(Nancy2) #Skip the first row 
    
    #insert records line by line
for row in Nancy2:
    mycursor.execute('INSERT IGNORE INTO Student( Student_ID, Student_Name, College_ID, Date_Joined, Major_Taken, College_Level) VALUES(%s,%s,%s,%s,%s,%s)',row)
mydb.commit() 
print("Records added to Student table")


# In[44]:


import mysql.connector as conn
import csv
mydb = conn.connect(
    host="localhost",
    user="root",
    password="nancywachira",
    database="Academics")

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM Student INNER JOIN college                 ON college.College_id = student.College_id                 INNER JOIN Professor ON college.College_id = Professor.College_id")
for x in mycursor.fetchall():
    print (x)
        


# In[ ]:




