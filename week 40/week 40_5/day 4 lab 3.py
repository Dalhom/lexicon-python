"""

3.
Learn how to use map() to apply a transformation to every item in a list.

Task:
Explain the purpose of map() and how it works in Python.
Create a real-life scenario where you need to modify every element of a list in the same way.

For example, you have a list of prices, and you want to apply a 10% discount to each.
How would you use map () with a lambda function to achieve this?


The map() function in Python applies a transformation (a function) to each item in an iterable (such as a list or tuple) 
and returns a map object (an iterator) with the transformed items. To use or display the results, you'll typically convert it
into a list, tuple, or another collection.
Essentially, it’s a way to apply a function to every element in a list (or another iterable) without writing a loop manually.

"""


# prices = [10.50, 13.1, 3.9, 8.0]
prices = [20, 10, 50, 80]

discount = list(map(lambda i: i * 0.9, prices))
print(discount)

