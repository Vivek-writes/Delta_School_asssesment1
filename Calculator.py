# A simple calculator using python


def add(x,y):
    return(x+y)
def subtract(x,y):
    return(x-y)
def multiply(x,y):
    return(x*y)
def divide(x,y):
    return(x/y)

while 1:
    print("Choose one option(1,2,3,4,5)")
    print("1 to ADD")
    print("2 to SUBTRACT")
    print("3 to MULTIPLY")
    print("4 to DIVIDE")
    print("5 to EXIT")
    option = input("enter option: ")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter Second number: "))

    if option == '1':
        print(num1, "+", num2, "=", add(num1,num2))
    elif option == '2':
        print(num1, "-", num2, "=", subtract(num1,num2))
    elif option == '3':
        print(num1, "*", num2, "=", multiply(num1,num2))
    elif option == '4':
        print(num1, "/", num2, "=", divide(num1,num2))
    elif option == '5':
        print("Exiting the program...")
        break  
    else:
        print("Invalid input")