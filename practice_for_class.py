class Car:
    # The __init__ method is the constructor that initializes the object
    def __init__(self, make, model, year):
        self.make = make        # Attribute to store car's make
        self.model = model      # Attribute to store car's model
        self.year = year        # Attribute to store car's year

    # Method to display car information
    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    # Method to start the car
    def start(self):
        print(f"The {self.make} {self.model} is now running.")


input_car_name = input("Enter your  car name: ")
input_car_make = input("Enter your car make model: ")
input_car_year = input("Enter your car make year: ")


# Create an object of the Car class
my_car = Car( input_car_name, input_car_make, input_car_year)

# Call methods on the object
my_car.display_info()  # This will display the car's info
my_car.start() 


