# TUPLES - like lists but immutable: cant change or append etc

# my_tuple = (1, 2, 3, 'four', 3)
# print(my_tuple[-1])
# print(my_tuple.index('four'))
# print(my_tuple.count(3)) # return number of occurences of a value

# SETS - unique values

# x = set()
# x.add(1)
# print(x) # outputs {}, not a dictionary as no key-value pair

# y = {1,2,3}
# y.add(4)
# y.add(3) # unchanged since set is used for unique elements
# print(y)

# my_list = [1, 2, 3, 1, 2, 3, 4, 5, 4, 6]
# print(set(my_list))

# BOOLEANS - True or False
# COMPARISONS: > < >= <= == !=

# a = True
# print(a)
# print(1>2)
# print(1=='1')

# LOGIC: and or 
# if: elif: else: ... and the importance of indentation (tab or 4 spaces)

# FOR LOOPS 
# sequence = [1, 2, 3, 4, 5]

# for item in sequence:
    # print(item)
    # print(item + item)

# ages = {
#     'John' : 4,
#     'Doe' : 8,
#     'Moe' :5
# }
#
# for key in ages:
#    print('This is the key:')
#    print(key)
#    print('This is the value: ')
#    print(ages[key])
#    print('/n')



# mypairs = [(1,10),(2,20),(3,30)]
# 
# for tup in mypairs: # contents of list ie iterate each of the 3 tuples
#     print(tup)
# 
# for item1, item2 in mypairs: # unpack the contents of each tuple
#     print(item1)
#     print(item2)

# for i in range(5):
#    print(i)

# for i in range(2,10,2): # range, last argument is step
#    print(i)

# WHILE LOOPS

# i = 1
# 
# while i < 5:
#    print('i is: {}'.format(i))
#    i += 1

# RANGE function with LIST function
#
# i = list(range(5))
# print (i)

x = [1, 2, 3]
out = []

for item in x:
    out.append(item**2)
print(out)

print([item **2 for item in x])