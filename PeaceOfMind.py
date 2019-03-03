from parents import *
from admin import *
from time import *

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
        elif(user[0] == "a"):  #input for admin
            AdminScript()
            sleep(2)
            user = ""
        elif(user[0] == "p"):  #input for parent
            ParentScript()
            sleep(2)
            user = ""
        elif(user[0] == "d"):   #input for driver
            print("You're a driver!")
            user = ""
        else:
            print("Invalid word, please try again.")
            user = ""
    print("Thank you for using PeaceOfMind")

if (__name__ == "__main__"):
    main()
