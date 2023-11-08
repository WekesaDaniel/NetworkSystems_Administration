def Operation ():
    Operation = input ("Specify operation to be executed :\n a for addition,\n s for subtraction,\n m for multiplication and\n d for division\n")
    if Operation == "a" :
        Sum ()
    elif Operation == "s" :
        Difference()
    elif Operation == "m" :
        Product ()
    elif Operation == "d" :
        Division ()
    else :
        print("Invalid operation specified ; please use given parameters")
def Sum ():
    First_number = int(input ("Enter first number\n"))
    Second_number = int(input ("Enter second number\n"))
    x= First_number+Second_number
    print("The sum is : ",x)
def Difference ():
    _FirstNumber = int(input ("Enter first number\n"))
    _SecondNumber = int(input ("Enter second number\n"))
    print("The difference is : ", _FirstNumber-_SecondNumber)
def Product ():
    first_number = int(input ("Enter first number\n"))
    second_number = int(input ("Enter second number\n"))
    print ("The procuct is : ", first_number*second_number)
def Division ():
    Number_1 = int(input ("Enter first number\n"))
    Number_2 = int(input ("Enter second number\n"))
    print(str(Number_1) +" "+ "Divided by " + str(Number_2) +" "+ "is: " , Number_1/Number_2)
Operation ()