
# Diagram of Python Program Execution for p1.py

# +---------------------+
# | Write Code in p1.py |
# +---------------------+
#           |
#           v
# +---------------------+
# | Run Python          |
# | Interpreter         |
# | (e.g. python p1.py) |
# +---------------------+
#           |
#           v
# +---------------------+
# | Compile to Bytecode |
# | (creates p1.pyc)   |
# +---------------------+
#           |
#           v
# +---------------------+
# | Execute Bytecode    |
# | in Python Virtual    |
# | Machine (PVM)       |
# +---------------------+
#           |
#           v
# +---------------------+
# | Output Result       |   
# +---------------------+


#Example:                       ***** Assigning multiple values to multiple variables *****

# 1:

# a, b, c = 5, 3.2, 'Hello'
# print (a)  # prints 5
# print (b)  # prints 3.2
# print (c)  # prints Hello 

# 2: 

# x=y="Hello World"
# print (x)  # prints programiz.com
# print (y)  # prints programiz.com


# 3:

# is_pass = True
# print(is_pass)# Output: True 


# 4: Character Literals in Python

# some_character = 'S'
# print(some_character)


# 5: Special Literal in Python

# value = None
# print(value)# Output: None

# 6: list literal
# fruits = ["apple", "mango", "orange"] 
# print(fruits)

# 7: tuple literal
# numbers = (1, 2, 3) 
# print(numbers)

# 8: dictionary literal
# alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} 
# print(alphabets)

# 9: set literal
# vowels = {'a', 'e', 'i' , 'o', 'u'} 
# print(vowels)




#Example:                     ***** Python Type Conversion *****


# There are two types of type conversion in Python.



# Implicit Conversion - automatic type conversion

# integer_number = 123
# float_number = 1.23
# new_number = integer_number + float_number
# print("Value:",new_number)
# print("Data Type:",type(new_number))


# Explicit Conversion - manual type conversion

# num_string = '12'
# num_integer = 23
# print("Data type of num_string before Type Casting:",type(num_string))
# # explicit type conversion
# num_string = int(num_string)
# print("Data type of num_string after Type Casting:",type(num_string))
# num_sum = num_integer + num_string
# print("Sum:",num_sum)
# print("Data type of num_sum:",type(num_sum))



#Example:                    ******* Syntax of print() ******

# print(object= separator= end= file= flush=)
# object - value(s) to be printed
# sep (optional) - allows us to separate multiple objects inside print().
# end (optional) - allows us to add add specific values like new line "\n", tab "\t"
# file (optional) - where the values are printed. It's default value is sys.stdout (screen)
# flush (optional) - boolean specifying if the output is flushed or buffered. Default: False

# print with end whitespace
# print('Good Morning!','It is rainy today', sep=' hey ')



#Example:                 ************* Python Arithmetic Operators *************

# 1: Floor Division
# print(10//3)
# 2: Power
# print(10**4)




#Example:                 ************* Python taking Input*************

# name = input("Enter your name: ")
# print("Hello, " + name + "!")

# num = int(input("Enter a number: "))
# print('The integer number is:',num)# , operator automatically add a space 
# print(f'The integer number is:{num}')# no mrore space 
# float_num = float(input("Enter a floating number: "))
# print(f'The floating number is: {float_num}')

# x, y = input("Enter two numbers separated by space: ").split()
# x = int(x)
# y = int(y)
# print(f'The sum of {x} and {y} is {x + y}.')



# Example:              ************* Python Flow Control ************* 


#          1: if else if 


# number =int(input("Enter a number: "))

# if number > 0:
#     print('Positive number')

# elif number < 0:
#     print('Negative number')

# else:
#     print('Zero')

# print('This statement is always executed')



#          2: For Loop

# languages = ['Swift', 'Python', 'Go']
# # Start of loop
# for lang in languages:
#     print(lang)

# language = 'Python'
# # iterate over each character in language
# for x in language:
#     print(x)

# iterate from i = 0 to i = 3
# for i in range(4):
#     print(i)

# for i in range(10):
#     if i>3:
#         break
#     print(i)


# for i in range(10):
#     if i>3:
#      continue
#     print(i) op:0,1,2,3


#           3: While Loop
# num=0
# while num<3:
#     print(num)
#     num=num+1

# Print numbers until the user enters 0
# number = int(input('Enter a number: '))

# # iterate until the user enters 0
# while number != 0:
#     print(f'You entered {number}.')
#     number = int(input('Enter a number: '))
# print('The end.')




# Example:             ************* Python Data types ************* 


# 1:          Python Random Module

# import random

# print(random.randrange(10, 20))

# list1 = ['a', 'b', 'c', 'd', 'e']
# list2=list1.copy()

# # get random item from list1
# print(random.choice(list1))

# # Shuffle list1
# random.shuffle(list2)

# # Print the shuffled list1
# print(list1)
# print(list2)


# # Print random element
# print(random.random())


# 2:             Python Mathematics
# import math

# print(math.pi)
# print(math.factorial(6))


#  3:               Python List

# fruits = ['apple', 'banana', 'orange']
# print('Original List:', fruits)

# # using append method 
# fruits.append('cherry')

# print('Updated List:', fruits)


# colors = ['Red', 'Black', 'Green']
# print('Original List:', colors)

# # changing the third item to 'Blue'
# colors[2] = 'Blue'

# print('Updated List:', colors)

# numbers = [2,4,7,9]

# # remove 4 from the list
# numbers.remove(4)

# print(numbers) 

# Output: [2, 7, 9]

# cars = ['BMW', 'Mercedes', 'Tesla']

# print('Total Elements: ', len(cars))  
  
# # Output: Total Elements:  3



# 4:            Python Tuple

# Tuple Cannot be Modified

# cars = ('BMW', 'Tesla', 'Ford', 'Toyota')

# # trying to modify a tuple
# cars[0] = 'Nissan'    # error
       
# print(cars)

# fruits = ('apple','banana','orange')

# # iterate through the tuple
# for fruit in fruits:
#     print(fruit)

# Check if an Item Exists in the Tuple
# colors = ('red', 'orange', 'blue')

# print('yellow' in colors)    # False
# print('red' in colors)       # True


#  5:     Python Strings

# greet = 'hello'

# # access 1st index element
# # print(greet[1]) # "e"
# # greet = 'hello'

# # access 4th last element
# print(greet[-4]) # "e"

# # access character from 1st index to 3rd index
# print(greet[1:4])  # "ell"

# Python Strings are Immutable
# message = 'Hola Amigos'
# message[0] = 'H'
# print(message) TypeError: 'str' object does not support item assignment


# multiline string 
# message = """
# Never gonna give you up
# Never gonna let you down
# """
# print(message)

# Compare Two Strings
# str1 = "Hello, world!"
# str2 = "I love Swift."
# str3 = "Hello, world!"
# # compare str1 and str2
# print(str1 == str2)
# # compare str1 and str3
# print(str1 == str3)

# Join Two or More Strings
# greet = "Hello, "
# name = "Jack"
# # using + operator
# result = greet + name
# print(result)
# # Output: Hello, Jack

# String Membership Test
# print('a' in 'program') # True
# print('at' not in 'battle') # False

# text= 'Split this string'

# # splits using space
# print(text.split())

# grocery = 'Milk, Chicken, Bread'

# # splits using ,
# print(grocery.split(', '))

# # splits using :
# # doesn't split as grocery doesn't have :
# print(grocery.split(':'))


# escape double quotes
# example = "He said, \"What's there?\""

# print(example)

# # escape single quotes
# example = 'He said, "What\'s there?"'

# print(example)

# # Output: He said, "What's there?"


# 6:                  Python Sets



# create a set of integer type
# student_id = {11,1,1100,33,33,33, 22, 114, 116, 118, 115, 115}
# print('Student ID:', student_id)

# # create an empty set
# empty_set = set()
# # create an empty dictionary
# empty_dictionary = { }
# # check data type of empty_set
# print('Data type of empty_set:', type(empty_set))
# # check data type of dictionary_set
# print('Data type of empty_dictionary:', type(empty_dictionary))

# numbers = {21, 34, 54, 12}
# print('Initial Set:',numbers)
# # using add() method
# numbers.add(32)
# print('Updated Set:', numbers) 

# companies = {'Lacoste', 'Ralph Lauren'} #set
# tech_companies = ['apple', 'google', 'apple'] #list
# # using update() method
# companies.update(tech_companies
# print(companies)
# Output: {'google', 'apple', 'Lacoste', 'Ralph Lauren'}

# # first set
# A = {1, 3, 5}
# # second set
# B = {0, 2, 4}
# # perform union operation using |
# print('Union using |:', A | B)
# # perform union operation using union()
# print('Union using union():', A.union(B)) 


# first set
# A = {2, 3, 5}
# # second set
# B = {1, 2, 6}
# # perform difference operation using &
# print('Difference using - :', A - B)
# # perform difference operation using difference()
# print('Difference using difference():', A.difference(B)) 


# 7:          Python Dictionary


# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
#   "England": "London"
# }
# # access the value of keys
# print(country_capitals["Germany"])    # Output: Berlin
# print(country_capitals["England"])    # Output: London


# Add Items to a Dictionary
# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
# }
# # add an item with "Italy" as key and "Rome" as its value
# country_capitals["Italy"] = "Rome"
# print(country_capitals)


# Remove Dictionary Items
# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
# }
# country_capitals.pop("Germany")
# print(country_capitals)
# # delete item having "Germany" key
# del country_capitals["Germany"]
# print(country_capitals)

# country_capitals = {
#   "Germany": "Berlin", 
#   "Canada": "Ottawa", 
# }
# # clear the dictionary
# country_capitals.clear()
# print(country_capitals)  

# country_capitals = {"England": "London", "Italy": "Rome"}
# # get dictionary's length
# print(len(country_capitals))   # Output: 2


# Example:            ************* Python Functions *************


# def greet(name):
#     print("Hello", name)
# # pass argument
# greet("John")


# def mul(num):
#     res=num*num
#     return res
# print(mul(3))



# def add_numbers( a = 7,  b = 8):
#     sum = a + b
#     print('Sum:', sum)
# # function call with two arguments
# add_numbers(2, 3)
# #  function call with one argument
# add_numbers(b = 2)
# # function call with no arguments
# add_numbers()



# program to find sum of multiple numbers 
# def find_sum(*numbers):
#     result = 0
#     for num in numbers:
#         result = result + num
#     print("Sum = ", result)
# # function call with 3 arguments
# find_sum(1, 2, 3)
# # function call with 2 arguments
# find_sum(4, 9)


# # declare global variable
# message = 'Hello'
# def greet():
#     # declare local variable
#     print('Local', message)
# greet()
# print('Global', message)



# outside function 
# def outer():
#     message = 'local'
#     # nested function  
#     def inner():
#         # declare nonlocal variable
#         nonlocal message
#         message = 'nonlocal'
#         print("inner:", message)
#     inner()
#     print("outer:", message)

# outer()

# # global variable
# c = 1 
# def add():
#      # increment c by 2
#     global c
#     c =c + 2
#     print(c)
# add()


# Example of a recursive function

# def fact(num):

#     if num==1:
#         return 1
#     else: 
#      return num*fact(num-1)
# print (fact(5))

# print(__name__)



#                         *********        Python Files         *********

# Get Current Directory in Python

# import os;
# print(os.getcwd())
# print(os.listdir())

# os.mkdir('test')
# os.listdir()
# ['test']


# os.listdir()
# ['test']
# # rename a directory
# os.rename('test','new_one')
# os.listdir()
# ['new_one']

# import shutil
# # delete "mydir" directory and all of its contents
# shutil.rmtree("test")


#                   Python CSV: Read and Write CSV Files

# read

# import csv
# with open('people.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# write

# import csv
# with open('innovators.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(["SN", "Name", "Contribution"])
#     writer.writerow([1, "Linus Torvalds", "Linux Kernel"])
#     writer.writerow([2, "Tim Berners-Lee", "World Wide Web"])
#     writer.writerow([3, "Guido van Rossum", "Python Programming"])

# with open('innovators.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)



#           ***********  Python Exceptions    ***********


# numerator = 10
# denominator = 0
# result = numerator/denominator
# print(result)


# print(dir(locals()['__builtins__']))


# 1:       Python try...except Block


# try:
#     numerator = 10
#     denominator = 0
#     result = numerator/denominator
#     print(result)
# except:
#     print("Error: Denominator cannot be 0.")


# 2:       Catching Specific Exceptions in Python

# try:
#     even_numbers = [2,4,6,8]
#     print(even_numbers[5])
# except ZeroDivisionError:
#     print("Denominator cannot be 0.") 
# except IndexError:
#     print("Index Out of Bound.")
# # Output: Index Out of Bound



#       Python try with else clause
# program to print the reciprocal of even numbers
# try:
#     num = int(input("Enter a number: "))
#     assert num % 2 == 0
# except:
#     print("Not an even number!")
# else:
#     reciprocal = 1/num
#     print(reciprocal)


#         Python try...finally

# try:
#     numerator = 10
#     denominator = 0
#     result = numerator/denominator
#     print(result)
# except:
#     print("Error: Denominator cannot be 0.")
# finally:
#     print("This is finally block.")



#               user-defined exceptions



# # define Python user-defined exceptions
# class InvalidAgeException(Exception):
#     "Raised when the input value is less than 18"
#     pass
# # you need to guess this number
# number = 18
# try:
#     input_num = int(input("Enter a number: "))
#     if input_num < number:
#         raise InvalidAgeException
#     else:
#         print("Eligible to Vote")    
# except InvalidAgeException:
#     print("Exception occurred: Invalid Age")


#          ************      Python Classes and Objects     ************


# # define a class
# class Bike:
#     name = ""
#     gear = 0
# # create object of class
# bike1 = Bike()
# # access attributes and assign new values
# bike1.gear = 11
# bike1.name = "Mountain Bike"
# print(f"Name: {bike1.name}, Gears: {bike1.gear} ")



# create a class
# class Room:
#     length = 0.0
#     breadth = 0.0 
#     # method to calculate area
#     def calculate_area(self):
#         print("Area of Room =", self.length * self.breadth)
# # create object of Room class
# study_room = Room()
# # assign values to all the properties 
# study_room.length = 42.5
# study_room.breadth = 30.8
# # access method inside class
# study_room.calculate_area()


# Constructor

# class Employee:
#     def __init__(self, name, age):
#         self.name = name  # Initialize the name attribute
#         self.age = age    # Initialize the age attribute
# # Create an instance of Employee
# employee1 = Employee("Disha", 33)
# # Accessing attributes
# print(employee1.name)  # Output: Disha
# print(employee1.age)   # Output: 33



# Python Inheritance

# class Animal:
#     name=""
#     def eat(self):
#         print("i can it")
# class Dog(Animal):
#     def display(self):
#         print(self.name)
# dog =Dog()
# dog.name="Dog"
# dog.eat()
# dog.display()


# Method Overriding in Python Inheritance

# class Animal:
#    name = ""    
#    def eat(self):
#         print("I can eat")
# # inherit from Animal
# class Dog(Animal):
#     # override eat() method
#     def eat(self):
#         # call the eat() method of the superclass using super()
#         super().eat()
#         print("I like to eat bones")
# # create an object of the subclass
# labrador = Dog()
# labrador.eat()


# Python Multilevel Inheritance


# class SuperClass:
#     def super_method(self):
#         print("Super Class method called")
# # define class that derive from SuperClass
# class DerivedClass1(SuperClass):
#     def derived1_method(self):
#         print("Derived class 1 method called")
# # define class that derive from DerivedClass1
# class DerivedClass2(DerivedClass1):
#     def derived2_method(self):
#         print("Derived class 2 method called")
# # create an object of DerivedClass2
# d2 = DerivedClass2()
# d2.super_method()  # Output: "Super Class method called"
# d2.derived1_method()  # Output: "Derived class 1 method called"
# d2.derived2_method()  # Output: "Derived class 2 method called"


#          Method Resolution Order (MRO) in Python

# class SuperClass1:
#     def info(self):
#         print("Super Class 1 method called")
# class SuperClass2:
#     def info(self):
#         print("Super Class 2 method called")
# class Derived(SuperClass1, SuperClass2):
#     pass
# d1 = Derived()
# d1.info()  
# # Output: "Super Class 1 method called"



#         Method Overriding

# from math import pi
# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def area(self):
#         return self.length**2

#     def fact(self):
#         return "Squares have each angle equal to 90 degrees."
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#     def area(self):
#         return pi*self.radius**2
#     def fact(self):
#         return "Circle have each angle equal to 360 degrees."

# a = Square(4)
# b = Circle(7)
# print(b.area())
# print(b.fact())
# print(a.fact())
# print(b.area())
