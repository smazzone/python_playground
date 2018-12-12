class Dog:
    """A simple class representing a dog"""

    #Every method call associated with an instance 
    # automatically passes self, which is a reference 
    # to the instance itself; it gives the individual 
    # instance access to the attributes and methods in 
    # the class. 
    # When we make an instance of Dog, Python will call 
    # the __init__() method from the Dog class. We’ll pass 
    # Dog() a name and an age as arguments; self is passed 
    # automatically, so we don’t need to pass it.
    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting"""
        print(f"{self.name} is now sitting, boss!")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} is now rolling over, boss!")

my_dog = Dog('Fuffy',3)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Black',4)
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()






