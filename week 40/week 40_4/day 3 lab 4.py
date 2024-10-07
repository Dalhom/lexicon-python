""""

4. Return the number of even integers in the given array/list.

Examples:
count_evens([2, 1, 2, 3, 4]) → 3

count_evens([2, 2, 0]) → 3
count_evens([1, 3, 5]) → 0

"""

def count_evens(a):

    count = 0
    for i in a:

        if (i % 2 == 0):
            count += 1
    
    return count


my_list = [1, 3, 5]
print(count_evens(my_list))