# 3. Write a program that creates a new tuple containing only the even numbers from a given tuple of integers.

my_tuple = (5, 3, 9, 4, 7, 6, 2)
sequence = []


for i in range(len(my_tuple)):

#    print('Reading', my_tuple[i])

   if my_tuple[i] % 2 == 0:
        sequence.append(my_tuple[i])
#        print('Added', my_tuple[i])

#print(sequence)

new_tuple = tuple(sequence)
print(new_tuple)
