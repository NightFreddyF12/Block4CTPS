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
3. Get an item at an index
4. Sort list
5. Random search
6. Linear search
7. Recursive binary search
8. Iterative binary search
9. Print list
10. Quit   """)
            if choice == "1":
                addToList()
            elif choice == "2":
                addABunch()
            elif choice == "3":
                indexValues()
            elif choice == "4":
                sortList(myList)
            elif choice == "5":
                randomSearch()
            elif choice == "6":
                linearSearch()
            elif choice == "7":
                binSearch = input("What number are you looking for?   ")
                recursiveBinarySearch(unique_list, 0, len(unique_list)-1, int(binSearch))
            elif choice == "8":
                binSearch = input("What number are you looking for?   ")
                result = iterativeBinarySearch(unique_list, int(binSearch))
                if result != -1:
                    print("Your number is at index position {}".format(result))
                else:
                    print("Your number is not found in that list, bud!")
            elif choice == "9":
                printLists()
            else:
                break
        except:
            print("You did a dumb! Did you do it right?")

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!    ")
    myList.append(int(newItem))
    #we need to think about errors!
    
def addABunch():
    print("We're gonna add a bunch of integers here!")
    numToAdd = input("How many integers would you like to add?   ")
    numRange = input("And how high would you like these numbers to go?   ")
    for x in range(0, int(numToAdd)):
        myList.append(random.randint(0, int(numRange)))
    print("Your list is now complete.")

def sortList(myList):
    #note that this is the first function we've built here that takes ARGUMENTS
    for x in myList:
        if x not in unique_list:
            unique_list.append(x)
    unique_list.sort()
    showMe = input("Would you like to see the unique values in your list? Y/N   ")
    if showMe.lower() == "y":
        print(unique_list)

def indexValues():
    print("At what index position do you want to search?")
    indexPos = input("Type an index position here:   ")
    print(myList[int(indexPos)])

def randomSearch():
    print("oH iM sO rAnDom!!!")
    print(myList[random.randint(0, len(myList)-1)])
    if len(unique_list) > 0:
        print(unique_list[random.randint(0, len(unique_list)-1)])

def linearSearch():
    print("We're gonna check out each item one at a time in your list! This sucks.")
    searchItem = input("Whatcha lookin' for, pardner?   ")
    for x in range(len(myList)):
        if myList[x] == int(searchItem):
            print("Your item is at index position {}".format(x))

def printLists():
    if len(unique_list) == 0:
        print(myList)
    else:
        whichOne = input("Which list do you want to see, sorted or un-sorted?   ")
        if whichOne.lower() == "sorted":
            print(unique_list)

def recursiveBinarySearch(unique_list, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if unique_list[mid] == x:
            print("Your number is at index position {}".format(mid))
            return mid
        elif unique_list[mid] > x:
            return recursiveBinarySearch(unique_list, low, mid - 1, x)
        else:
            return recursiveBinarySearch(unique_list, mid + 1, high, x)
    else:
        print("Your number isn't here!")

def iterativeBinarySearch(unique_list, x):
    low = 0
    high = len(unique_list)-1
    mid = 0
    while low <= high:
        mid = (high + low) // 2
        if unique_list[mid] < x:
            low = mid + 1
        elif unique_list[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1
    
if __name__ == "__main__":
    mainProgram()
