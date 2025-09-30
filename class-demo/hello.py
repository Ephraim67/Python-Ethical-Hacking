# # This line is running python code without a variable
# print("Hello world!")
# print('I am learning python')


# # Declaring a variable
# f_name = "Ephraim"
# l_name = "Norbert"

# # Concatenation (concatenating a variable)
# print(f_name + " " + l_name)

# """
# Types of variables
# Integer whole number (eg: 0-9)
# floating-point (float) - Decimam numbers (e.g: 0.1)
# String (str) - Text Data ("hello", "Python", 'Text')
# Boolean (bool) - True/false values
# """

# age = 18
# sentence = "The legal age to vote in"
# country = "Tanzania"

# full_sentence = sentence + " " + country

# print(full_sentence + " is " + str(age))


# # Today's class (Friday's class)
# # Dictionationary is a collection of key-value pairs
# # Example of a dictionary
# cars = {'BMW': 'X6', 'Mercedes': 'GLC300', 'Tesla': 'Model X', 'Audi': 'Q3'}
# print(cars['Mercedes'])

# # List is a collection of items
# fruits = ['orange', 'bannana', 'apple', 'pineapple', 'mango', 'grep']

# # Calling item in a list by their index number
# # Indexing starts from 0
# # Example of indexing
# # fruits[0] = 'orange'
# # fruits[1] = 'bannana'
# # fruits[2] = 'apple'
# print(fruits[0])
# print(fruits[1])
# print(fruits[2])
# print(fruits[3])
# print(fruits[4])
# print(fruits[5])
# print(fruits[1:5])

# # Builtin function to add item
# fruits.append('test')

# # Remove an item
# fruits.remove('mango')
# print(fruits)

# # looping through an item multiple time using for statement
# # identation works with control flow
# # for fruits in fruits:
# #     print(fruits)

# # print an item in ranges
# for i in range(5):
#     print(fruits)

# # comment out with short cut (ctrl + /)

# # Looping through a line of code using while statement
# count = 0
# while count <= 100:
#     print("count: ", + count)
#     count += 2 # increment

# # dEFINING A FUNCTION
# def new_function(sum): # Parameter
#     return sum

# print(4+4) # value


# # name = input("What is your name: ")
# # print("My name is " + name)

# change_ip = input("Type your IP addr: ")
# print("Your IP has been changed to " + change_ip)

# ---------------------------------------------------------------------------------------

# Todays class (Tuesday - 08/04/2025)
# 1. Functions

# Creating a function
def greet():
    print("Good morning")

# Calling a function
greet()

# Pass an argument to a function
def greet(name):
    print("Good morning " + name)

# Passing an argument to a function
"""greet("Ephraim")
greet("Norbert")
greet("Juma")"""

# A parameter is a variable in a function definition
# An argument is the value you pass to a function when you call it
# Function with multiple parameters

def greet(f_name, l_name):
    print("Good morning " + f_name + " " + l_name)

# Calling a function with multiple parameters
greet("Ephraim", "Norbert")
greet("Juma", "Mwanakombo")

# Python Try Except
# Handling exceptions
# The 'try' block lets you test a block of code for errors
# The 'except' block lets you handle the error
# The 'else' block lets you execute code when there is no error
# The 'finally' block lets you execute code regardless of the result of the try-except block

# Example of try except
try:
    print(x) # This will cause an error because x is not defined
except:
    print("An error occurred") # This will be executed if there is an error


# Many exceptions
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Somthing else went wrong")

# Else statement
# Else is executed when there is no error
try:
    print("Hello")
except:
    print("An error occurred")
else:
    print("No error occurred")

# Finally statement
# The finally block is always executed, regardless of whether an error occurred or not
try:
    print(x)
except:
    print("An error occurred")
finally:
    print("x will not always executed as long as it's not defined.")

# Practicalizing everything
# We will create a file that is not writable and try to mofify it.
try:
    f = open("demo.txt", "r") # Open a file in read mode
    f = open("demo.txt", "w") # Open a file in write mode
    try:
        f.write("Hello world")
    except:
        print("Something went wrong when editing this file.")
    finally:
        f.close()
except:
    print("File not found")

finally:
    print("Any file that does not have write permission will not be able to be modified.")

# If condiitional statement
# If statement is used to check a condition
# If the condition is true, the code inside the if block will be executed
# If the condition is false, the code inside the else block will be executed

age = input("Enter your age: ")
if age < 18:
    if age == 18:
         print("You are 18 years old")
         print("You are a minor")
    else:
        print("You are not a minor")
elif age > 18:
    print("You are an adult")
else:
    print("You are not an adult")


sum = 10
if sum < 10:
    print("Sum is zero")
elif sum >= 10:
    print("Sum is positive")
else:
    print("Sum is negative")

#A function is a block of code that only runs when it is called.

# You can pass data, known as parameters, into a function.







