def greet_user(username):
    """Display a simple message"""
    print(f"Hello {username}!")

greet_user('Stefano')

""" When you use default values, any parameter with a 
default value needs to be listed after all the parameters 
that don’t have default values. This allows Python to 
continue interpreting positional arguments correctly.
"""

def describe_pet(pet_name, animal_type = 'cat'):
    """Display info about a pet"""
    print(f"Animal Type: {animal_type.title()}")
    print(f"Animal Name: {pet_name.title()}")

describe_pet('fuffy','hamster')
describe_pet(animal_type='dog',pet_name='willy')
describe_pet('romeo')

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


def get_formatted_name(first_name,last_name):
    """Return a full formatted name"""
    full_name=f"{first_name} {last_name}"
    return full_name.title()

musician=get_formatted_name('stefano',"mazzone")
print(musician)


def get_formatted_name(first_name, last_name,middle_name=''):
    """Return a full formatted name"""
    #Python interprets non-empty strings as True, 
    # so if middle_name evaluates to True if a middle name 
    # argument is in the function call
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician=get_formatted_name('stefano',"mazzone")
print(musician)
musician=get_formatted_name('stefano',"mazzone","francesco")
print(musician)


def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person"""
    person = {'first': first_name, 'last': last_name}
    #In conditional tests, None evaluates to False.
    if age:
        person['age'] = age
    return person

musician = build_person('stefano','mazzone')
print(musician)
musician = build_person('stefano','mazzone',52)
print(musician)



