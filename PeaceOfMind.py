from parents import *
from admin import *
from driver import *
from time import *

#creates .txt files if they do not exist for the program
try:
    openfile = open("IDS.txt", "r")
    openfile.close()
except:
    openfile = open("IDS.txt", "w+")
    openfile.close()
try:
    openfile = open("Drivers.txt", "r")
    openfile.close()
except:
    openfile = open("Drivers.txt", "w+")
    openfile.close()

def main():
    print("Welcome to PeaceOfMind")
    user = ""

    
    while(not(user)):
        user = input("Please login as <Admin>, <Parent>, or <Driver>.\n"
                     +"Type <leave> to logout: ")
        user = user.lower()
        if(user == ""):  #Invalid word used
            print("nothing inputed, try again")
        elif(user == "leave"):
            break
        elif(user[0] == "a"):  #activates Admin Login
            AdminScript()
            sleep(1)
            user = ""
        elif(user[0] == "p"):  #activates parent login
            ParentScript()
            sleep(1)
            user = ""
        elif(user[0] == "d"):   #activates driver login
            DriverScript()
            sleep(1)
            user = ""
        else:
            print("Invalid word, please try again.")
            user = ""
    print("Thank you for using PeaceOfMind")

if (__name__ == "__main__"):
    main()
