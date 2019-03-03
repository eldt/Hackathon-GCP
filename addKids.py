from random import *

def grabStoreddata(vector):
    infile = open("IDS.txt", "r")
    for line in infile:
        vector.append(line[:-1])
    infile.close()

def askForNewInput():
    string = input("Please insert \"<Your child's name>, <parent's name>\": ")
    return string.split(", ")

def addEntry(S, P, vector):
    hasID = 1
    find = 0
    IDNumb = "{0:0>6}".format(0)
    while(find != -1):
        find = -1
        for i in range(len(vector)):
            find = vector[i].find(str(IDNumb))
            if(find != -1):
                break
        if (find != -1):
            IDNumb = randrange(1,1000000)
            IDNumb = "{0:0>6}".format(IDNumb)
            find = -1

    print("Student name: " + S)
    print("Student ID: " + IDNumb)
    print("Guardian name: " + P)

    vector.append(S + " " + IDNumb + " " + P)
    
def writeFile(vector):
    outfile = open("IDS.txt", "w")

    for i in range(len(vector)):
        line = vector[i]
        print(line, file=outfile)

    outfile.close()

#==========================================
def addKids():
    stu = ""
    par = ""
    users = []
    grabStoreddata(users)
    
    stu, par = askForNewInput()
    addEntry(stu, par, users)
    
    writeFile(users)

def main():
    addKids()


if (__name__ == "__main__"):
    main()
