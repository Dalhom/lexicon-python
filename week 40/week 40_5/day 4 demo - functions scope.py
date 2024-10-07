#Lambda function - nameless

"""
def timesTwo(num):
    return num  * 2

lambda num: num * 2

"""

# take function and list and return only if True

lst = [1,2,3,4,5,6,7,8,9,10]

""" 
def evenBool(num):
    return num % 2 == 0

evens = filter(evenBool, lst) # using function
print(list(evens)) 

evens = filter(lambda num: num % 2 == 0, lst) # same result as above with one line using Lambda
print(list(evens)) 


res = map(lambda x: x +1, lst) #how to transform a list in a quick a readable way
print(list(res)) # output [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

# NB highlight, alt plus up/down to move into comments



def mapper(helper_func, iterable):
    result = []

    for value in iterable:
        helper_result = helper_func(value)
        result.append(helper_result)

    return result
    
values = [1,2,3,4,5]
result = mapper(lambda x:x - 1, values)

print(list(result))



# LEGB rules re SCOPE
# Local: variables inside the current function
# Enclosing: variables in enclosing functions (nested functions)
# Global: variables defined at the top level of the module or script
# Built-in: Python's built in names eg len() or range()

x = 15

def printer():
    x = 30
    return x

print(x) # global x = 15
print(printer()) # local x = 30
print(x) # global x = 15

--

name = 'Derek'

def greet():
    name = 'Erik'

    def hello():
        print('Hello ' + name) # refers to the name within greet ie enclosing scope

    hello() 

greet()
print('Hello ' + name) # prints global value

"""

# modify global variable

x = 50

def func():
    global x
    print('This function is now using global x')
    print('Because global x is ', x)

    x = 2
    print('Ran func() and changed global x to', x)

print('Before calling func(), x is: ', x)
func()
print('Value of x outside of func() is still ',x) # because global is used, global variable is used amd modified



