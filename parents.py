def userinput(string):
    IP = ""
    while(not(IP)):
        IP = str(input(string))
        if(IP == ""):  #Invalid word used
            print("nothing inputed, try again")
        elif(IP == "leave"):
            break
    return IP

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
        word = userinput("What do you want to do? ")
                


def main():
    ParentScript()

if(__name__ == "__main__"):
    main()
