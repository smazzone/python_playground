def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

def greet_users(names):
    for name in names:
        msg = f"Hello {name.title()}"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

def print_models(unprinted_design, completed_models):
    """Simulate printing each design"""
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"printing model: {current_design}...")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Display completed models"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models=[]

#The slice notation [:] makes a copy of the list to send to the function
#so that we do not modify the original list
print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)


#passing an arbitrary number of arguments
#*toppings is an emptty tuple
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms', 'green peppers', 'extra cheese')




#The double asterisks before the parameter **user_info cause 
# Python to create an empty dictionary called user_info and pack 
# whatever name-value pairs it receives into this dictionary. 
# Within the function, you can access the key-value pairs in 
# user_info just as you would for any dictionary.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',location='princeton',field='physics')
print(user_profile)