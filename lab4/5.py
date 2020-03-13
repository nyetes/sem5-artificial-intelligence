list=[1,2,3,4,5,56,6,8,9,0]
#print(list[3])
##print(list[3:5])
#print(list[-1])
#print(list[0:4:2])
print(list[::-1])

# palindrome
str=input("Enter string")
rev=str[::-1]
if (str==rev):
    print("palindrome")
else:
    print("not palin")