"""

4.
Learn how to combine the functionality of  filter() and map() to both select and modify elements in a list.

Task:
Describe a scenario where you need to filter out unwanted elements from a list and then modify the remaining elements.
For example, you might first filter a list to keep only positive numbers, and then square those numbers.
Break down the process of applying filter () first, and then using map() on the filtered result.

"""

# square only odd numbers

my_list = [1,2,3,4,5,6,7]

odd_nums = list(filter(lambda num: num % 2 == 1, my_list))
print(odd_nums)

squares_list = list(map(lambda i: i ** 2, odd_nums))
print(squares_list)

# square positive numbers

other_list = [-1, 4, -16, 8, -64]

positives = list(filter(lambda num: num > 0, other_list))
positive_squared = list(map(lambda i: i ** 2, positives))
print(positive_squared)