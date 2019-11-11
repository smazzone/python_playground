import json

def greet_user():
    """Greet the user by name."""
    filename = 'user.json'
    #try to load the json file otherwise prompt the user for input
    username = get_stored_username(filename)
    if username:
        print(f"Welcome back {username}!")
    else:
        username = get_username(filename)
        print(f"We will remember you {username}!")

def get_username(filename):
    print(f"filename: {filename}")
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username


def get_stored_username(filename):
    try:
        with open(filename,'r') as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

greet_user()