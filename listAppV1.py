"""
Program Goals:
1. Get input from the user (at multiple points) 
2. We need to convert some of this input to INTs from STRs
3. We need to provide choices to the user
    a. Add more values to a list
    b. Return a value at a specific index

"""

def mainProgram():
    while true:
        myList = []
        print("Hello, there! Let's work with lists!")
        print("Choose from the following options. Type a number below!")
        choice = input("""1. Add to a list or
    2. Return the value at an index position
    3. Exit Program   """)
        #add a way to catch bad user input
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            break
        #TO ADD: 1. A way to loop the action, 2. A way to quit, 3. Think of repitition

def addToList():
    print("Adding to a list! Great choice!")
    newItem = input("Type an integer here!    ")
    myList.append(int(newItem))

def indexValues():
    print("Ohhh! I heard you need a particular piece of data!")
    indexPos = input("What index position are you curious about?   ")
    myList[int(indexPos)]
    print(myList[int(indexPos)])


#dunder main -> Double Underscore---dunder
if __name__ == "__main__":
    mainProgram()
