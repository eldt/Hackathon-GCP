from location import *

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

    while(word != "leave"):
        word = userinput("What do you want to do? \n[1] Check in student\n[2] List students\n[3] Get location\n[0] Logout\n")
        if(word == '1'):
            stuID = input("Enter the student's ID number: ")
            infile = open("Buses.txt", "r")
            busVect = []
            for line in infile:
                busVect.append(line[:-1])

     #       for i in range (len(busVect)):
      #          print(busVect[i])
                
            infile.close
            for i in range(len(busVect)-1):
                if(busVect[i].find(str(route))):
                   stuVect = str(busVect[i])
                   busVect.pop(i)
            print(stuVect)
            busVect.append(stuVect + " " + stuID)
            outfile = open("Buses.txt", "w")
            for i in range (len(busVect)):
                line = busVect[i]
                print(line, file=outfile)
            outfile.close()
        if(word == '2')
            print("This should print the students on the bus")
        if(word == '3')
            a = input("Input a latitide: ")
            b = input("Input a longitude: ")
            a = float(a)
            b = float(b)
            GeoScript(a,b)
        if(word == '0')
            break


def main():
    DriverScript()

if(__name__ == "__main__"):
    main()
