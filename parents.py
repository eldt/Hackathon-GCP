# Checks if an input string is valid
def userinput(string):
    IP = ""
    while(not(IP)):
        IP = str(input(string))
        if(IP == ""):  #Invalid word used
            print("nothing inputed, try again")
        elif(IP == "leave"):
            break
    return IP

# Defines what a valid string is
def checkvalid(ID):
    find = -1
    empty = 0
    while((find == -1) and not(empty)):
        infile = open("IDS.txt", "r")
        for line in infile:
            find = line.find(ID)
            if(find != -1):
                  print("ID was found")
                  return True, line
            else:
                  empty = 1
        infile.close()
    if(find == -1):
            print("ID is was not found, try again or leave.")
            return False, line  

# Primary function, prompts login with a student ID, then lists options.
def ParentScript():
    word = ""
    line = ""
    stu = ""
    par = ""
    ID = ""
    valid = False
    while(word != "leave"):
        while(not(valid)):
            word = userinput("Please login with your student's ID: ")
            if(word == "leave"):
              break
            else:
                word = "{0:0>6}".format(int(word))
                valid, line = checkvalid(word)
        stu, ID, par = line[:-1].split(" ")
        print("")
        print("Your (the parent's) name: " + par)
        print("StudentName: " + stu)
        print("Student ID: " + ID)
        word = userinput("What do you want to do?\n[1] Check notifications\n[2] Edit notification preferences\n[0] Logout\n")
        if(word == '1'):
            print("This is where notifications should be displayed. The code is still in progress.")
        if(word == '2'):
            print("This is where you can choose which notifications you want to recieve. The code is still in progress.")
        if(word == '0'):
            break


def main():
    ParentScript()

if(__name__ == "__main__"):
    main()
