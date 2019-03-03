#admin.py

from addKids import *
from popKids import *

adminName = "Admin"
option = 0

# Displays a submenu for managing students
def manageStudents():
    print("What would you like to do?")
    # list and define options
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

# Displays every line in a file.
def listFile(file):
    infile = open(file, "r")
    for line in infile:
        print(line[:-1])
    print()
    infile.close()

# Displays a submenu for managing transportation
def manageTransportation():
    print("What would you like to do?")
    # list and define options
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

# Associates the ID of a driver with the route they will drive.
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

    # Display what has been added.
    print("Driver: " + driver)
    print("Route: " + route)

    driveVect.append(driver + " " + route)

    #Write to the file.
    outfile = open("Drivers.txt", "w")
    for i in range (len(driveVect)):
        line = driveVect[i]
        print(line, file=outfile)

    outfile.close()

def manageRoute():
    route = input("What route number? ")
    stops = input("Enter the stops of the route in the form: x-coordinate,y-coordinate x-coordinate,y-coordinate, ...")
    #if the route doesn't exist, add it to the file. If it does, delete the original first.
    stopsVect = []
    infile = open ("Stops.txt", "r")
    for line in infile:
        stopsVect.append(line[:-1])
    infile.close()

    find = 0
    while(find != -1):
        find = -1
        for i in range(len(stopsVect)):
            find = stopsVect[i].find(str(route))
            if(find != -1):
                stopsVect.pop(i)
                break
        if (find != -1):
            find = -1
    # Display what has been added.
    print("Route: " + route)
    print("Stops: " + stops)

    stopsVect.append(route + " " + stops)

    #Write to the file.
    outfile = open("Stops.txt", "w")
    for i in range (len(stopsVect)):
        line = stopsVect[i]
        print(line, file=outfile)

    outfile.close()
    
# Displays a list of students currently on a specified bus, as well as that bus' GPS coordinates.
def viewBus():
    input("View the bus on which route? ")
    #The rest of this function should be defined in the driver area of the code. Displays current GPS location, and a list of all students currently on that bus.

# Primary function, displays a menu of functions to access.
def AdminScript():

    print("Welcome, ",adminName,"!")
    print("What would you like to do?")
    # list and define options
    option = input("[1] Manage Students\n[2] Manage Transportation\n[0] Logout\n")

    while(option != '0'):
        if (option == '1'):
            manageStudents()
        elif (option == '2'):
            manageTransportation()
        else:
            print("Invalid input, please try again.")
            
        option = input("[1] Manage Students\n[2] Manage Transportation\n[0] Logout\n")


# Allows this program to be easily accessed by others.
def main():
    AdminScript()

if(__name__ == "__main__"):
        main()
