"""
Program Goals:
1. Get input from the user (at multiple points) 
2. We need to convert some of this input to INTs from STRs
3. We need to provide choices to the user
    a. Add more values to a list
    b. Return a value at a specific index

"""

import random
myList = []
unique_list = []

def mainProgram():
    while True:
        try:
            print("Hello, there! Let's work with lists!")
            print("Choose from the following options. Type a number below!")
            choice = input("""1. Add to a list
2. Add a bunch of numbers
3. Return the value at an index
4. Random search
5. Linear search
6. Sort list
7. Quit Program   """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                randomSearch()
            elif choice == "5":
                linearSearch()
            elif choice == "6":
                sortList(myList)
            else:
                break
        except:
            print("You did a dumb! Did you do it right?")

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!    ")
    myList.append(int(newItem))
    
def addABunch():
    print("We're gonna add a bunch of integers here!")
    numToAdd = input("How many integers would you like to add?   ")
    numRange = input("And how high would you like these numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete.")

def indexValues():
    print("Ohhh! I heard you need a particular piece of data!")
    indexPos = input("What index position are you curious about?   ")
    print(myList[int(indexPos)])

def sortList(myList):
    print("A little birdie told me you needed some sorted data!")
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Wanna see your new list?   Y/N")
    if showMe.lower() == "y":
        print(unique_list)

def randomSearch():
    print("RaNdOm SeArCh?!?")
    print(myList[random.randint(0, len(myList)-1)])

def linearSearch():
    print("We're gonna check out each item one at a time in your list! This sucks.")
    searchItem = input("Whatcha lookin' for, pardner?   ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position ()".format(x))

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list? Sorted or unsorted?    ")
        if whichOne.lower == "sorted":
            print(unique_list)
        else:
            print(myList)

#def password():
    #answer == "*t4],DTvTL7pR;cTW/+R3Rl;BY~SNYk=)h@Tmeu\SV"
    #if input == "Password":
        #try:
            #print("What is the password?")
            #if answer == "*t4],DTvTL7pR;cTW/+R3Rl;BY~SNYk=)h@Tmeu\SV":
                #print("The Answer to the Ultimate Question of Life, the Universe, and Everything... is 42")
            #else:
                #print("WRONG!")
        #break

if __name__ == "__main__":
    mainProgram()
