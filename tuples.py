# When compared with lists, tuples are simple data structures. 
# Use them when you want to store a set of values that should NOT 
# be changed throughout the life of a program.
dimensions = (200,50)
print(dimensions[0],dimensions[1])
#tuples are immutable, this will throw an exception
#dimensions[0] = 250

#but you can always associate a new tuple to dimensions
dimensions = (400,100)
for dimension in dimensions:
    print(dimension)