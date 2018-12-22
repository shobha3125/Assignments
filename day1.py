print("\n")
print("Question 1: Concatenate two strings\n")
name=input("what is your name :")
fname=input("what is your father's name :")
## Error Handling
if(name == "" or fname == ""):
	print("Error: Please enter a valid string")
	name=input("what is your name :")
	fname=input("what is your father's name :")
fullName = name+" " +fname
print("Your full name is : ", fullName)
print("+++++++++++++++++++++++++++++++++++++++++++++\n")

print("\n")
print("Question 2: Add two numbers\n")
print("Enter the numbers you want to add")

num1=input("Number1 : ")
num2=input("Number2 : ")
## Error Handling
if(num1 == "" or num2 == ""):
	print("Error: Please enter a valid number\n")
	num1=input("Number1 : ")
	num2=input("Number2 : ")
res=int(num1)+int(num2)
print("Result : ", res)
print("+++++++++++++++++++++++++++++++++++++++++++++\n")

print("Question 3: Find max of two number\n")
num3=input("Number1 : ")
num4=input("Number2 : ")
## Error Handling
if(num3 == "" or num4 == ""):
	print("Error: Please enter a valid number\n\n")
	num3=input("Number1 : ")
	num4=input("Number2 : ")
print("Result:")
if(int(num3) > int(num4)):
	print(num3 + " is greater than " + num4)
else:
	print(num4 + " is greater than " + num3)


print("+++++++++++++++++++++++++++++++++++++++++++++\n")
print("\n")
from math import sqrt
print("Question 4: from math import sqrt\n")
num5=input("Enter a number to find the square root: ")
## Error Handling
if(num5 == ""):
	print("Error: Please enter a valid number\n\n")
	num5=input("Enter a number to find the square root: ")
print("Square root of num5 is: ", sqrt(int(num5)))

print("+++++++++++++++++++++++++++++++++++++++++++++\n")
print("\n")
print("Question 5: import math\n")
import math

print("Enter two numbers to find powerof\n")
num6=input("Number1 : ")
num7=input("Number2 : ")
## Error Handling
if(num6 == "" or num7 == ""):
	print("Error: Please enter a valid number\n\n")
	num6=input("Number1 : ")
	num7=input("Number2 : ")
print("power of : ", num6, num7 )
print("is ", math.pow(int(num6), int(num7)))

print("+++++++++++++++++++++++++++++++++++++++++++++\n")
