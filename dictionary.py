""" A dictionary in Python is a collection of key-value pairs. 
Each key is connected to a value, and you can use a key to access 
the value associated with that key. A key’s value can be a number, 
a string, a list, or even another dictionary. 
In fact, you can use any object that you can create in Python as a 
value in a dictionary.
In Python, a dictionary is wrapped in braces, {}, with a series 
of key-value pairs inside the braces, as shown in the earlier example:
 """
alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)


alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")




alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

alien_0['speed'] = 'fast'

   # Move the alien to the right.
   # Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")


alien_0 = {
    'color': 'green', 
    'points': 5,
    'size:':'large'
    }
print(alien_0)

del alien_0['points']
print(alien_0)

""" It’s good practice to include a comma after the last key-value 
pair as well, so you’re ready to add a new key-value pair on the next line.
 """
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print(favorite_languages)

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is: {language}")


alien_0 = {'color': 'green', 'speed': 'slow'}
#you get an exception as points key does not exist
#print(alien_0['points'])

#but you can use get method + default in case of missing key
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

""" If you leave out the second argument in the call to get() 
and the key doesn’t exist, Python will return the value None. 
The special value None means “no value exists.” This is not an 
error: it’s a special value meant to indicate the absence of a value. """


user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key,value in user_0.items():
    print(f"key: {key} value: {value}")

#which is abbreviated here
for k,v in user_0.items():
    print(f"key: {k} value: {v}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

for name in favorite_languages.keys():
    print(name.title())

""" Looping through the keys is actually the default 
behavior when looping through a dictionary, so this code 
would have exactly the same output if you wrote """

for name in favorite_languages:
    print(name.title())


friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\tHey {name.title()}, I see you love {language}!")


if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

#sorting dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    'alice': 'go',
    }

print("------sorted dictionary-------")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")







favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("This is a set of unique values:")
#To see each language chosen without repetition, 
# we can use a set. A set is a collection in which each item must be unique:

for language in set(favorite_languages.values()):
    print(language.title())

#You can build a set directly using braces and separating the elements with commas:
languages = {'python', 'ruby', 'python', 'c'}
print(languages)

#It’s easy to mistake sets for dictionaries because they’re both wrapped in braces. 
# When you see braces but no key-value pairs, you’re probably looking at a set. 
# Unlike lists and dictionaries, sets do not retain items in any specific order.


#a list of dictionary

alien_0 = {'color':'green', 'points':5}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'blue', 'points':15}
alien_3 = {'color':'red', 'points':25}

aliens = [alien_0,alien_1, alien_2, alien_3]

for alien in aliens:
    print(alien)


aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    print(f"creating alien: {alien_number}...")


for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10


for alien in aliens[:5]:
    print(alien)
print("...")

   # Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")

# Store information about a pizza being ordered.
# a dictionary containing a list of toppings
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

i=0
for topping in pizza['toppings']:
    i=i+1
    print(f"\t{i}-" + topping)
    

#a dictionary containing multiple lists
favorite_languages = {
       'jen': ['python', 'ruby'],
       'sarah': ['c'],
       'edward': ['ruby', 'go'],
       'phil': ['python', 'haskell'],
       }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
    else:
        print(f"\n{name.title()}'s favorite languages is:")
    for language in languages:
        print(f"\t-{language.title()}")


# a dictionary nested into another dictionary

users = {
       'aeinstein': {
           'first': 'albert',
           'last': 'einstein',
           'location': 'princeton',
           },

       'mcurie': {
           'first': 'marie',
           'last': 'curie',
           'location': 'paris',
           },
       }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")