import sqlite3 as sql
import os
from functools import partial

def newContact(personName, personPhone):
    conn = sql.connect("contact-book.db")
    conn.cursor()
    conn.execute("INSERT INTO contact_book (name, phone) VALUES (?, ?)", (personName, personPhone))
    conn.commit()
    conn.close()

    os.system('cls')

def viewContact():   
    conn = sql.connect("contact-book.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM contact_book')
    
    query = cursor.fetchall()
    print(query)

def deleteContact(personName):
    conn = sql.connect("contact-book.db")
    conn.cursor()
    conn.execute("DELETE FROM contact_book WHERE name = ?", [personName])
    conn.commit()
    conn.close()

    os.system('cls')

def updateContact(personID, personName, personPhone):
    conn = sql.connect("contact-book.db")
    conn.cursor()
    conn.execute("UPDATE contact_book SET name = ?, phone = ? WHERE id = ?", (personName, personPhone, personID))
    conn.commit()
    conn.close()

conn = sql.connect("contact-book.db")
conn.cursor()
conn.execute("CREATE TABLE IF NOT EXISTS contact_book (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(100), phone VARCHAR(30))")
conn.commit()
conn.close()

print("Let's add some contacts")

while True:
    print("Choose a option from below")
    print("[1] - Add new contact")
    print("[2] - View all contacts")
    print("[3] - Delete a contact")
    print("[4] - Update a contact")
    print("[5] - Leave")
    userOption = int(input("Option > "))

    if userOption == 1: #Add New Contact
        personName = input("Type a new name > ")
        personPhone = input(f'Type a phone for {personName} > ')
        newContact(personName, personPhone)

    elif userOption == 2: #View all Contacts
        viewContact()

    elif userOption == 3: #Delete one Contact
        personName = input("Type a name you want to delete > ")
        deleteContact(personName)

    elif userOption == 4: #Update one Contact
            print("Which ID contact you want to update?")
            personID = int(input("Type the person's ID > "))
            personName = input("Type the new name > ")
            personPhone = input("Type the new phone > ")

            updateContact(personID, personName, personPhone)

    elif userOption == 5:
        print("You choose to leave the program")

    else:
        print("Invalid Option")
