""""

3. Given a string, return a string where for every char in the original,
# there are two chars.

doubleChar('The') → 'TThhee'
doubleChar('AAbb') → 'AAAAbbbb'
doubleChar('Hi-There') → 'HHii--TThheerree'

"""

def doubleChar(a):
    
    new_string = ''

    for i in range(0, len(a)):
        new_string += a[i] + a[i]

    print(new_string) 

string = 'Hi-There'
doubleChar(string)
    