# ****************************************************************************************************
#
#       Name:          Joi Wilson
#       Course:        COSC 2110 Computer Languages: Python
#       Assignment:    PhoneBook.py
#       Due Date:      11/25/2020
#       Description:
#                      The phonebook driver program
#
# ****************************************************************************************************

import sqlite3
from sqlite3 import Error


# ****************************************************************************************************

def display_all(database, tableName):
    connection = sqlite3.connect(database)

    rows = connection.execute("SELECT * FROM " + tableName)

    print("")

    for row in rows:
        print("{0}\t\t{1}".format(row[1], row[2]))

    connection.close()


# ****************************************************************************************************

def create_row(database, tableName):
    name = input("Name: ")
    phone = input("Phone number: ")

    connection = sqlite3.connect(database)

    connection.execute("INSERT INTO " + tableName + " (Name, Phone) VALUES(?, ?)", \
                       (name, phone))

    print("New entry added")

    connection.commit()

    connection.close()


# ****************************************************************************************************

def read_row(database, tableName):
    searchName = input("Searching for? : ")

    connection = sqlite3.connect(database)

    rows = connection.execute("SELECT * FROM " + tableName + " WHERE Name LIKE " + "'" + searchName + "%'")

    print("")

    for row in rows:
        print("{0}\t\t{1}".format(row[1], row[2]))

    connection.close()


# ****************************************************************************************************

def update_row(database, tableName):

    searchName = input("Searching for? : ")

    connection = sqlite3.connect(database)

    rows = connection.execute("SELECT * FROM " + tableName + " WHERE Name LIKE " + "'" + searchName + "%'")


    print("ID\tName\t\tPhone")
    for row in rows:
        print("{0}\t{1}\t{2}".format(row[0], row[1], row[2]))

    idNo = input("Enter the ID of the entry you wish to update: ")
    newName = input("Enter the new name: ")
    newPh = input("Enter the new phone number: ")

    connection.execute("UPDATE " + tableName + " set Name= " + "'" + newName + "'" + \
                       ", Phone= " + "'" + newPh + "'" + " where EntryID = " + idNo)

    print("entry updated")

    connection.commit()

    connection.close()


# ****************************************************************************************************

def delete_row(database, tableName):

    searchName = input("Name to search for: ")

    connection = sqlite3.connect(database)

    rows = connection.execute("SELECT * FROM " + tableName + " WHERE Name LIKE " + "'" + searchName + "%'")

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM " + tableName + " WHERE Name LIKE " + "'" + searchName + "%'")

    if len(cursor.fetchall()) == 0:
        print("Not found")

        connection.close()
        return

    print("ID\tName\t\tPhone")
    for row in rows:
        print("{0}\t{1}\t{2}".format(row[0], row[1], row[2]))

    idNo = input("Enter the ID of the entry you wish to delete: ")
    choice = input("Are you sure? (y/n): ")

    if choice != "y":

        connection.close()
        return

    connection.execute("DELETE FROM " + tableName + " WHERE EntryID = " + idNo)

    print("Entry deleted.")

    connection.commit()

    connection.close()


# ****************************************************************************************************

def main():

    database = "phonebook.db"
    tableName = "Entries"

    while True:
        print("\t\tMENU\t\t")
        print("------------------------------------")
        print("1 - Display All")
        print("2 - Create a New Phonebook Entry")
        print("3 - Read a Phonebook Entry")
        print("4 - Update a Phonebook Entry")
        print("5 - Delete a Phonebook Entry")
        print("6 - EXIT")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            display_all(database, tableName)
        elif choice == 2:
            create_row(database, tableName)
        elif choice == 3:
            read_row(database, tableName)
        elif choice == 4:
            update_row(database, tableName)
        elif choice == 5:
            delete_row(database, tableName)
        elif choice == 6:
            break

        print("\n")


if __name__ == '__main__':
    main()
