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
            listFile("IDS.txt")
        else:
            print("Invalid input, please try again.")

        option = input("[1] Add a student\n[2] Delete a student\n[3] List students and guardians\n[0] Go back\n")

def listFile(file):
    infile = open(file, "r")
    for line in infile:
        print(line[:-1])
    print()
    infile.close()

def manageTransportation():
    print("What would you like to do?")
    option = input("[1] Add or modify a driver\n[2] Manage routes\n[3] View a bus\n[4] List drivers\n[0] Go back\n")

    while(option != '0'):
        if (option == '1'):
            modDriver()
        elif (option == '2'):
            manageRoute()
        elif (option == '3'):
            viewBus()
        elif (option == '4'):
            listFile("Drivers.txt")
        else:
            print("Invalid input, please try again.")

        option = input("[1] Add or modify a driver\n[2] Manage routes\n[3] View a bus\n[4] List drivers\n[0] Go back\n")    

def modDriver():
    driver = input("Enter a driver ID: ")
    route = input("Which route will this driver take? ")
    #if the driver doesn't exist, add it to the file. If it does, delete the original first.
    infile = open("Drivers.txt", "r")
    driveVect = []
    for line in infile:
        driveVect.append(line[:-1])
    infile.close()
    find = 0
    while(find != -1):
        find = -1
        for i in range(len(driveVect)):
            find = driveVect[i].find(str(driver))
            if(find != -1):
                driveVect.pop(i)
                break
        if (find != -1):
            find = -1

    print("Driver: " + driver)
    print("Route: " + route)

    driveVect.append(driver + " " + route)

    outfile = open("drivers.txt", "w")
    for i in range (len(driveVect)):
        line = driveVect[i]
        print(line, file=outfile)

    outfile.close()

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
            
        option = input("[1] Manage Students\n[2] Manage Transportation\n[0] Logout\n")

def main():
    AdminScript()

if(__name__ == "__main__"):
        main()
