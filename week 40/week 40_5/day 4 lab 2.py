"""

2.
Understand how to use filter() in Python with a lambda function to select elements from a list that meet a certain condition.
Task:
Explain what filter () does in Python and what kind of result it returns.
Create an example scenario where you need to filter out elements from a list.
For instance, you are given a list of numbers, and you need to keep only the even numbers. How would you approach this using filter ()?

"""

my_list = [1,2,3,4,5,6,7,8,9]

new_list = list(filter(lambda num: num % 2 == 0, my_list))
print(new_list)

