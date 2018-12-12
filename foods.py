my_foods = ['pizza', 'falafel', 'carrot cake']

""" 
To copy a list, you can make a slice that includes the entire original list by 
omitting the first index and the second index ([:]). This tells Python to make a 
slice that starts at the first item and ends with the last item, producing a copy 
of the entire list.
"""

friend_foods = my_foods[:]
my_foods.append('pasta')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)