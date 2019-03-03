#admin.py

from addKids import *
from popKids import *

adminName = "Admin"
option = 0

def manageStudents():
    print("What would you like to do?")
    option = input("[1] Add a student\n[2] Delete a student\n[3] List students and guardians\n[0] Go back\n")

    while(option != '0'):
        if (option == '1'):
            addKids()
        elif (option == '2'):
            popKids()
        elif (option == '3'):
            listStudents()
        else:
            print("Invalid input, please try again.")

        option = input("[1] Add a student\n[2] Delete a student\n[3] List students and guardians\n[0] Go back\n")

def listStudents():
    infile = open("IDS.txt", "r")
    for line in infile:
        print(line[:-1])
    print()
    infile.close()

def manageTransportation():
    print("What would you like to do?")
    option = input("[1] Add or modify a driver\n[2] Manage routes\n[3] View a bus\n[0] Go back\n")

    while(option != '0'):
        if (option == '1'):
            modDriver()
        elif (option == '2'):
            manageRoute()
        elif (option == '3'):
            viewBus()   
        else:
            print("Invalid input, please try again.")

        option = input("[1] Add or modify a driver\n[2] Manage routes\n[3] View a bus\n[0] Go back\n")    

def modDriver():
    input("Enter a driver name/ID: ")
    #if the driver doesn't exist, add it to the file
    input("Which route will this driver take? ")
    #associate with the new driver, or replace the route of an existing driver with this new one.

def manageRoute():
    input("What route number? ")
    #if the route exists, delete it and start over. Otherwise, add it.
    input("Define the route, in the form: Road name, Distance on that road, Name, Distance, ... , Name, Distance\n")
    #write the route to the file
    input("Enter the stops of the route in the form: Stop name, Coordinates of stop, Name, Coordinates, ... , Name, Coordinates\n")
    #write the stops to the other file

def viewBus():
    input("View the bus on which route? ")
    #The rest of this function should be defined in the driver area of the code. Displays current GPS location, and a list of all students currently on that bus.


def AdminScript():

    print("Welcome, ",adminName,"!")
    print("What would you like to do?")
    option = input("[1] Manage Students\n[2] Manage Transportation\n[0] Logout\n")

    while(option != '0'):
        if (option == '1'):
            manageStudents()
        elif (option == '2'):
            manageTransportation()
        else:
            print("Invalid input, please try again.")
            
        option = input("[1] Manage Students\n[2] Remove a student\n[3] Manage Drivers\n[0] Logout\n")

def main():
    AdminScript()

if(__name__ == "__main__"):
        main()
