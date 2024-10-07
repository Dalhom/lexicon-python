"""

1. Given a list of integers, return True if the sequence of numbers 1, 2, 3
appears in the list somewhere.

Example:

arrayCheck([1, 1, 2, 3, 1]) → True
arrayCheck([1, 1, 2, 4, 1]) → False
arrayCheck([1, 1, 2, 1, 2, 3]) → True

"""

def arrayCheck(a):

    if len(a) > 2:

        for i in range(len(a)-2):

            if a[i] == 1 and a[i+1] == 2 and a[i+2] == 3:
                return True

        return False

    else:
        print('The list needs to have three numbers or more')

my_list = [1, 1, 2, 1, 2, 3]

print(arrayCheck(my_list))