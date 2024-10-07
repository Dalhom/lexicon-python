# 2. Write a program that calculates the sum of all elements in a given tuple.

tuple = (5, 3, 9, 4)
total = 0

for i in range(len(tuple)):
    total += tuple[i]

print('The sum is: ', total)
print('The sum is also: ',sum(tuple))