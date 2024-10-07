# def any_name(parameter='default'):  # defines the function with any descriptive name, optional (multiple) parameter (with a value if needed) as an input
"""
This function prints the value of the parameter (dark string triple quotes enables multi line comment)
"""
    
#     print(parameter, 'hello') # needs indentation

# any_name()

""""
def hello():
    return 'hello'


res = hello()
print(res)

print(hello) #wrong way - prints the 'location' of the function in memory
print(hello()) # right way to print


def evenCheck(number):
    if number % 2==0: # if the remainder when divided by 2 is 0, it's even
        return 'Even'
    else:
        return 'Odd'
    
print(evenCheck(10))
print(evenCheck(7))

# shorter version

def evenCheck(number):
    print(number % 2 == 0)

evenCheck(7)



def helloYou(name='John'):
    return 'Hello ' + name

print (helloYou('Bob')) # overwrites the value



def addEvenOnly(num1,num2):
    if num1 % 2 != 0 or num2 % 2 != 0: # if either number is odd
        return False
    
    else:
        return num1 + num2
    
print(addEvenOnly(1,2))
print(addEvenOnly(2,4))



def func(a, b, c=10, d=11):
    print(a, b, c, d)

func(1,2) # prints 1 2 10 11, other values use the default
func(1, 2, 3) # prints 1 2 3 11, overwrites default value



def func(*args): # non keyword arguments, when you dont know how many arguments
    print(args) # prints a tuple

func(1,2,3)



def func(a,b,**kwargs): # put key arguments into a dictionary, double star ('kwargs' is convension, any name will do)
    print(a,b) # prints a tuple
    print(kargs) # prints a dictionary

func(1,2,c=14,d=18)



def func2(a, b, **kwargs):
    print(a,b)
    if 'c' in kwargs:
        print(kwargs['c'])

func2(1, 2, c=14)



def func3(a, b, *args, name='John', **kwargs):
    print('a = {}'.format(a))
    print('b = {}'.format(b))
    print('args = {}'.format(args))
    print('name = {}'.format(name))
    print('kwargs = {}'.format(kwargs))

func3(1,2)
func3(1,2,3,name="Anna",age=34)

"""
# recursion

def factorial(n):
    #base case: stops the infinite loop so a stackoverflow error wont occur
    if n == 0:
        return 1
    
    #recursive case
    else:
        return n * factorial(n - 1) # calls itself
    

res = factorial(5)
print(res)    # will print outermost recursion result (stops at innermost)
