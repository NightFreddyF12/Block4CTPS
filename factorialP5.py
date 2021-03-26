def factorial(x):

    if x == 1:
        return 1
    else:
        return(x * factorial(x-1))

if __main__ == "__name__":

    num = input("What do you want the factorial of?   ")
    print("The factorial of " , num , " is ", factorial(int(num)))
