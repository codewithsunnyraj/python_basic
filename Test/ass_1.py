# Q1. Which keyword is used to create a function? Create a function to return a list of odd numbers in the
# range of 1 to 25.
l1=[]
def oddNumber(l):
    for i in l:
        if i % 2 != 0:
            l1.append(i)
    return l1



# print(list(range(0,26)))

print(oddNumber(list(range(0,26))))


# Q2. Why *args and **kwargs is used in some functions? Create a function each for *args and **kwargs
# to demonstrate their use.
"""
*args is used to accept any number of positional arguments.
It collects them into a tuple.

**kwargs is used to accept any number of keyword arguments
(key-value pairs). It collects them into a dictionary.
"""

def sumOfNo(*args):
    b = 0
    for i in args:
     b = b + i
    return b

print(sumOfNo(1,2,3,4,5,6))

def keyPair(**kwargs):
   return kwargs

print(keyPair(a=10,c=15,x=["radhe radhe"],y=15))
# print(keyPair(key=value,key=value,key=value,))


# Q3. What is an iterator in python? Name the method used to initialise the iterator object and the method
# used for iteration. Use these methods to print the first five elements of the given list [2, 4, 6, 8, 10, 12, 14,
# 16, 18, 20].

"""
--> An iterator in Python is an object that allows us to access elements of an iterable (such as a list, tuple, or dictionary) one at a time.



--> Methods used in an iterator
__iter__() — Initializes or returns the iterator object.

__next__() — Returns the next element from the iterator. When no elements remain, it raises a StopIteration exception.

--> Important distinction
for and while are loops, not iterator methods.

iter() calls the __iter__() method.

next() calls the __next__() method.
"""

numbers = [2, 4, 6, 8, 10, 12, 14,16, 18, 20]

# it = iter(numbers)  # Creates an iterator using __iter__()

# print(next(it))     # Gets the next element using __next__()
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

# Q4. What is a generator function in python? Why yield keyword is used? Give an example of a generator function

"""
A generator function is a special type of function that returns values one at a time instead of returning all values at once. It uses the yield keyword to produce values. Generator functions are memory-efficient because they generate values only when needed.

## The yield keyword is used to:

--> Return a value from a generator function.
--> Pause the function's execution temporarily.
--> Resume execution from where it paused when the next value is requested.
--> Save the function's current state between calls.

####   Difference between return and yield: ### 
-->>>> return terminate the function but
-->>>> yield pauses the function and allows it to continue later

"""

def numbers():
   yield 10
   yield 20
   yield 30

gen = numbers()
print(next(gen))
print(next(gen))
print(next(gen))

# Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
# first 20 prime numbers.



# Q6. Write a python program to print the first 10 Fibonacci numbers using a while loop.

# Q7. Write a List Comprehension to iterate through the given string: ‘pwskills’.
# Expected output: ['p', 'w', 's', 'k', 'i', 'l', 'l', 's']


# Q8. Write a python program to check whether a given number is Palindrome or not using a while loop.


# Q9. Write a code to print odd numbers from 1 to 100 using list comprehension.
# Note: Use a list comprehension to create a list from 1 to 100 and use another List comprehension to filter
# out odd numbers.


# MCQ
# What is the purpose of a function in Python?

        # To break up a program into smaller, reusable pieces of code
        #  To store data in memory
        # To perform a specific task or set of tasks
        # To control the flow of a program

# What is the syntax for defining a function in Python?

        # define function_name(arguments):
        # function function_name(arguments):
        # def function_name(arguments)
        #  create function_name(arguments):

# What are parameter passing in Python?

        # The process of sending data to a function as input
        #  The process of storing data in memory
        # The process of returning data from a function
        #  The process of manipulating data in a function


# What is the purpose of iterators in Python?

        # To repeat a block of code a specified number of times
        #  To allow for efficient access to elements in a sequence one at a time
        # To store data in memory
        # To manipulate data in a function



# What is a generator function in Python?

        # A function that generates a sequence of values
        #  A function that creates an iterator
        # A function that performs a specific task or set of tasks
        #  A function that breaks up a program into smaller, reusable pieces of code


# What is the difference between a normal function and a generator function in Python?

        #   Normal functions return a single value, while generator functions return an iterator
        # Normal functions use the return statement, while generator functions use the yield statement
        # Normal functions can only be used once, while generator functions can be used multiple times
        #  Normal functions can only return numbers, while generator functions can return any type of data



