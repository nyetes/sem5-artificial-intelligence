# Lab 3
# QN 4 Implementation of IF-ELSE by finding the greatest number among three entered numbers.
a= int (input ("Enter first number \n"))
b= int (input ("Enter second number \n"))
c= int (input ("Enter third number \n"))
if a>b & a>c:
    print (f"{a} is the greatest number")
elif b>a & b>c:
    print (f"{b} is the greatest number")
else:
    print (f"{c} is the greatest number")