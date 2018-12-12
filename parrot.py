message = input("Please tell me something and I will repeat it! ")
print(message)


name = input("Please enter your name: ")
print(f"\nHello, {name.title()}!")


prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")


age = input("How old are you? ")
if int(age) >= 18:
    print("you can vote")