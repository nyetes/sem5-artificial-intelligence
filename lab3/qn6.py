# Lab 3
# QN6 Display the factorial of an entered number
fact = 1
a = int(input("Enter any number \n"))
b=a
while (a > 0):
    fact = fact * a
    a -= 1
print (f"The factorial of {b} is {fact}")