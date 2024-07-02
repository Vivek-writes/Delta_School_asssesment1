#Program to show the implementatioin of error handling
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is {result}")
    except ZeroDivisionError:
        print("Error: You cannot divide by zero!")
    except TypeError:
        print("Error: Both inputs must be numbers!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


divide_numbers(10, 2)
divide_numbers(10, 0)  
divide_numbers("10", 2)  
divide_numbers(10, "2")  