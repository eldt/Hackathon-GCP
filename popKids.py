from random import *

def grabStoreddata(vector):
    infile = open("IDS.txt", "r")
    for line in infile:
        vector.append(line[:-1])
    infile.close()

def askForInput():
    string = input("Please insert the ID you wish to delete: ")
    return string

def DeleteEntry(S, vector):
    find = -1
    while(find == -1):
        for i in range(len(vector)):
            find = vector[i].find(S)
            if(find != -1):
                temp = vector[i].split(" ")
                print(temp[0] + " has been deleted.")
                vector.pop(i)
                break
        if (find == -1):
            print("ID does not exist.")
            break
            
    
def writeFile(vector):
    outfile = open("IDS.txt", "w")

    for i in range(len(vector)):
        line = vector[i]
        print(line, file=outfile)

    outfile.close()

#==========================================
def popKids():
    stu = ""
    par = ""
    users = []
    grabStoreddata(users)
    
    stu = askForInput()
    DeleteEntry(stu, users)
    
    writeFile(users)

def main():
    popKids()


if (__name__ == "__main__"):
    main()
