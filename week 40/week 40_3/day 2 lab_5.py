# 5. Write a program that takes a list of integers as input and uses list comprehension to create a new list containing only the even numbers from the original list.

my_list = input ("Enter your list of integers separated by spaces: ")
new_list = list(map(int, my_list.split()))
even_list = [num for num in new_list if num % 2 == 0]
print(even_list)