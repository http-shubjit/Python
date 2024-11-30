
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



