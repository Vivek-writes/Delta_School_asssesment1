#Problem:- Define a function that takes a list of numbers and returns the sum of these numbers.


def sum(list1):
    sum = 0
    for a in list1:
        sum = sum + a
    print("List:",list1)    
    print("Sum :", sum)

 
list1= []

length = int(input("Enter the no. of elements: "))

print("Enter the elements: ")
for i in range(length):
    x = int(input())
    list1.append(x)

sum(list1)