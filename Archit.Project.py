# 1. Write a Python program to take a user's first name and last name
# and print them together in the format: "Hello, [First Name] [Last Name]!"
"""
def my_function(fname,lname):
    print(fname,lname)
fname1 = (input("Enter first name :", ))
lname1 = (input("Enter last name:",  ))
my_function(fname1,lname1 )
"""
from tempfile import tempdir

'''
def my_function(fname, lname):
  print( fname, lname)

my_function("Archit", "Singh")
'''
# 2. Write a Python program that takes an integer input from the user and checks if it is positive, negative, or zero.
"""
def mynum(num):
    if x == 0:
        print("Number is zero")
    elif x>=0:
        print("Number is positive")
    else:
        print("Number is negative")
x = int(input("Please Enter Any Number : " , ))
mynum(x)
"""

# 3. Write a Python program to swap the values of two variables using a temporary variable.
"""
x = 5
y = 10
def myfunc(x,y):
    temp = x
    x = y
    y = temp
    print(x)
    print(y)
myfunc(x,y)
"""

# 4. Write a Python program to calculate the area of a circle
# using the formula `Area = π * r^2`. Take the radius `r` as input.
'''
def area_of_circle(r):
    area = (3.14 * r * r)

    print(area)
r = int(input("enter the number : ", ))
area_of_circle(r)
'''

# 5. Write a Python program to convert a temperature from Fahrenheit to Celsius
# using the formula: `C = (F - 32) * 5/9`.
'''
def far_to_cel(farhenheit):
    celsius = (farhenheit-32)*5/9
    print(celsius)
temp_c = float(input("enter the value: ", ))
far_to_cel(temp_c)
'''

# 6. Write a Python program that takes 5 numbers as input from the user and stores them in a list.
#  and Print the list.

'''
def mylist(a):
    print(a)
a = list(input("enter any five numbers: ", ))
mylist(a)
'''

# 6. Write a Python program that takes 5 numbers as input from the user and stores them in a list. Print the list.
'''
def mylist(r):
    print(r)
x = (list(input("enter an five numbers: ", )))
mylist(x)
'''

# 13. Write a Python program to generate the multiplication table for a number input by the user (up to 10).
'''
n = int(input("Enter The Number: ", ))
for i in range (1,11):
    x= i*n
    print(x)
'''
'''
def myfun(z):
    for i in range(1,11):
        x = i*n
        print(x)
n = int(input("enter the number: " , ))
myfun(n)
'''


# 14. Write a Python program using nested loops to print a pattern like this:
"""
    1
    1 2
    1 2 3
    1 2 3 4
    1 2 3 4 5
"""
'''

i = 5
while i <=5:
    print(i*1)
    i = i + 1
'''

# 15. Write a Python program that iterates through a string and counts the number of vowels in it.
'''
x = "hello world"
vowel = ("a","e","i","o","u","A","E","I","O","U")
for i in x:
    if i in vowel:
        print(i)

'''

# 16. Write a Python program to create a dictionary
# where the keys are names and values are ages.
# Add three entries and print the dictionary.
'''
mydict = {
    "amit" : 30,
    "pooja": 25,
    "sumit": 18
}
print(mydict)
'''

# 17. Write a Python program to update a key-value pair in a dictionary.
# The program should replace an existing age with a new one.


'''
mydict = {
    "amit" : 30,
    "pooja": 25,
    "sumit": 18
}
mydict["pooja"] = 29
print(mydict)
'''
# 18. Write a Python program to check if a specific key exists in a dictionary.

'''
mydict = {
    "amit" : 30,
    "pooja": 25,
    "sumit": 18
}

x = "pooja"
if x in mydict:
    print(x)
'''

# 19. Write a Python program to create a dictionary and print all the keys and values separately.
'''
mydict = {
    "amit" : 30,
    "pooja": 25,
    "sumit": 18
}
for x in mydict.keys():
    print(x)
for y in mydict.values():
    print(y)
'''

# 20. Write a Python program to take an integer input and check if the number is even or odd.
'''
x = int(input("Enter the number : " , ))
if x % 2 == 0:
    print([x] ,"is even")
else:
    print([x]," is odd")
'''

# 21. Write a Python program to check whether a given year is a leap year.
'''
x = int(input("enter the year: " , ))
if x % 4 == 0:
    print([x],"is leap year")
else:
    print([x],"is not a leap year")
'''



# 22. Write a Python program to accept three numbers from the user
# and print the largest of the three using an if-else statement.
'''
n1 = float(input("Enter the first number: "))
n2 = float(input("Enter the second number: "))
n3 = float(input("Enter the third number: "))

if n1 >= n2 and n1 >= n3:
    print(n1)
elif n2 >= n1 and n2 >= n3:
    print(n2)
else:
    print(n3)
'''
# 23. Write a Python program to check if a character input is a vowel or consonant.
'''
x =(input("enter the character : " ))
vowel = ("a","e","i","o","u","A","E","I","O","U")
if x in vowel:
    print([x], "is vowel")
else:
    print([x],"is consonant")
'''

# 24. Write a Python program to check if a given string is a palindrome.
'''
text = input1("Enter any word to check is it PALINDROME or not:- ")

reversed_text = text[::-1]

if text == reversed_text:
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
'''
# 25. Write a Python program to find the factorial of a number using a loop.


#30. Write a Python program to create a simple calculator
# that performs addition, subtraction, multiplication, and division
# based on user input.
"""
print("SIMPLE CALCULATER:->")
print("Enter (1) for Addition ___________(+):")
print("Enter (2) for Subtraction_________(-):")
print("Enter (3) for Multiplication______(*):")
print("Enter (4) for Division____________(%):")

x = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if x == '1':
    print(num1 + num2)
elif x == '2':
    print(num1 - num2)
elif x == '3':
    print(num1 * num2)
elif x == '4':
    print(num1 % num2)
else:
    print("invalid operation")
"""

# 5. Write a Python program to convert a temperature from Fahrenheit to Celsius
# using the formula: `C = (F - 32) * 5/9`.

'''
def cel_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
temp_f =cel_to_fahrenheit(23)
print("Temperature in Fahrenheit: ", temp_f)
'''
# 25. Write a Python program to find the factorial of a number using a loop.
'''
def add():
    print("Addition Of Two Numbers ")

    a = int(input("Enter First Number: " ) )
    b = int(input("Enter Second Number: " ) )
    c = a+b
    return c
s = add()
print("sum of the number is:-" , s)
'''

#SI CALCULATOR
'''
p = int(input('P: '))
n = int(input('N: '))
r = int(input('R: '))
si = (p*n*r)/100
print("Simple Interest:", si)

'''
#code for checking number is less , equal , or greater

'''
a = int(input("enter the number:-"))
b = int(input("enter second number:-"))
if a < b:
    print(f"{a} is less than {b}")
elif a > b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} is equal to {b}")
    
'''
'''
# code for simple calculator
method = input("Enter the operation (+,-,*,/):-")
input1 = int(input("Enter first number:- "))
input2 = int(input("Enter second number:- "))
if method == '+':
    print(f"The addition of {input1} and {input2} is:- {input1+input2}")
elif method == '-':
    print(f"The subtraction of {input1} and {input2} is:- {input1-input2}")
elif method == '*':
    print(f"The multiplication of {input1} and {input2} is:- {input1*input2}")
elif method == '/':
    print(f"The division of {input1} and {input2} is:- {input1/input2}")
else:
    print("None")
print("THANK YOU FOR USING THIS CALCULATOR")

'''
#print (a) 5 times using while loop

'''
number = 1
while number <= 5:
    print('a')
    number = number+1
'''
