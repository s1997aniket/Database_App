import psycopg2
from tkinter import *
import tkinter as tk

root = Tk()
canvas = Canvas(root, height = 500, width = 500)
canvas.pack()

frame = Frame()
frame.place(relx=0.3, rely=0.1, relwidth=0.8, relheight=0.8)

# Create the table
def create():
    conn = psycopg2.connect(dbname="postgres", user="postgres", password="Abcd1234!@#$", host = "localhost", port="5432" )
    cur = conn.cursor()
    cur.execute('''CREATE TABLE STUDENT(ID SERIAL, NAME TEXT, AGE TEXT, ADDRESS TEXT);''')
    print("Table Created!")
    conn.commit()
    conn.close()

# Drop the table
def drop():
    conn = psycopg2.connect(dbname="socratica_tutorial", user="postgres", password="Abcd1234!@#$", host = "localhost", port="5432" )
    cur = conn.cursor()
    cur.execute('''DROP TABLE STUDENT;''')
    print("Table Deleted!")
    conn.commit()
    conn.close()

# Getting the data
def get_data(name, age, address):
    conn = psycopg2.connect(dbname="socratica_tutorial", user="postgres", password="Abcd1234!@#$", host = "localhost", port="5432" )
    cur = conn.cursor()
    
    query = '''INSERT INTO student (NAME, AGE, ADDRESS) VALUES (%s,%s,%s);'''
    cur.execute(query, (name, age, address))   

    print("Data Inserted!")
    display_all()
    conn.commit()
    conn.close()


def search(id):
    conn = psycopg2.connect(dbname="socratica_tutorial", user="postgres", password="Abcd1234!@#$", host = "localhost", port="5432" )
    cur = conn.cursor()
    
    query = '''select * from student where id = %s;'''
    cur.execute(query, (id))

    row = cur.fetchone()    
    display_search(row)
    
    conn.commit()
    conn.close()


def display_search(row):
    listbox = Listbox(frame, width=20, height=5)
    listbox.grid(row=9,column=1)
    listbox.insert(END,row)

def display_search_2(row):
    listbox = Listbox(frame, width=20, height=5)
    listbox.grid(row=10,column=1)

    for x in row:
        listbox.insert(END,x)

def display_all():
    conn = psycopg2.connect(dbname="socratica_tutorial", user="postgres", password="Abcd1234!@#$", host = "localhost", port="5432" )
    cur = conn.cursor()
    
    query = '''select * from student;'''
    cur.execute(query)

    row = cur.fetchall()    
    display_search_2(row)

    conn.commit()
    conn.close()


# Creating the labels
button = Button(frame, text = "Create", command=lambda:create())
button.grid(row=0, column=2)

button = Button(frame, text = "Drop", command=lambda:drop())
button.grid(row=0, column=3)


label = Label(frame, text="Add Data: ")
label.grid(row = 0, column = 1)

# Name
label = Label(frame, text="Name ")
label.grid(row = 1, column = 0)

entry_name = Entry(frame)
entry_name.grid(row=1, column=1)

# Age
label = Label(frame, text="Age ")
label.grid(row = 2, column = 0)

entry_age = Entry(frame)
entry_age.grid(row=2, column=1)

# Address
label = Label(frame, text="Address ")
label.grid(row = 3, column = 0)

entry_address = Entry(frame)
entry_address.grid(row=3, column=1)

button = Button(frame, text = "Add", command=lambda:get_data(entry_name.get(),entry_age.get(), entry_address.get()))
button.grid(row=4, column=1)

# Search Function
label = Label(frame, text="Search Data")
label.grid(row = 5, column = 1)

label = Label(frame, text="Search by ID")
label.grid(row = 5, column = 1)

id_search = Entry(frame)
id_search.grid(row=6, column=1)

button = Button(frame, text = "Search", command=lambda:search(id_search.get()))
button.grid(row=6, column=2)




root.mainloop()