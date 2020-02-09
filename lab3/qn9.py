# Lab 3
# QN 9 Creating function to calculate the sum and difference of two numbers entered by user.

def mySum(a,b):
    return a+b
def myDiff(a,b):
    return a-b
num1=int(input("Enter 1st num\n"))
num2=int(input("Enter 2nd num \n"))
sum=mySum(num1,num2)
diff=myDiff(num1,num2)
print(sum)
print(diff)