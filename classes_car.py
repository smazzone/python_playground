class Car:
    """A simple class which models a car"""
    def __init__(self, make, model, year):
        """Initialize a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        print("initializing a new car...")

    def get_descriptive_name(self):
        """return a formatted name"""
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name

    def read_odometer(self):
        """print the mileage of the car"""
        print(f"The car mileage is: {self.odometer_reading}")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You cannot roll back an odometer!!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Fill gas tanks."""
        print("filling gas tank...")

# my_new_car = Car("audi","a1",2015)
# print(my_new_car.get_descriptive_name())
# my_new_car.update_odometer(23)
# my_new_car.read_odometer()
# my_new_car.update_odometer(21)
# my_new_car.read_odometer()
# my_new_car.increment_odometer(20_000)
# my_new_car.read_odometer()



