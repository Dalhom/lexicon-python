"""

2. Given a string, return a new string made of every other character starting
with the first, so "Hello" yields "Hlo".

Example:

stringBits('Hello') → 'Hlo'
stringBits('Hi') → 'H'
stringBits('Heeololeo') → 'Hello'

"""

def stringBits(a):
    
    new_string = ''

    for i in range(0, len(a), 2):
        new_string += a[i]

    print(new_string) 

string = 'Heeololeo'
stringBits(string)