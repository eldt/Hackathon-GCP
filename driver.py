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
        infile = open("Drivers.txt", "r")
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

def DriverScript():
    word = ""
    line = ""
    ID = ""
    route = ""
    valid = False
    while(word != "leave"):
        while(not(valid)):
            word = userinput("Please login with your ID: ")
            if(word == "leave"):
              break
            else:
                word = "{0:0>6}".format(int(word))
                valid, line = checkvalid(word)
        ID, route = line.split(" ")
        print("")
        print("Your ID is: " + ID)
        print("Your Route# is: "+ route)

        word = userinput("What do you want to do? ")
                


def main():
    DriverScript()

if(__name__ == "__main__"):
    main()
