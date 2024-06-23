# The parent class that defines vehicle type, in this case it'll be car
class Vehicle():
    def __init__(self, type):
        self.type = 'car'

    # This helps make the end result look cleaner when it prints it
    def user_vehicle_type(self):
        print("Vehicle Type:", self.type)
    
# The Automobile class which inherits from the Vehicle class type
class Automobile(Vehicle):
    def __init__(self, type):
        # inheriting type from Vehicle class
        super().__init__(type)
        # Setting the different parts to this for the user to enter their input
        self.year = input("Please enter the year your car was made.")
        self.make = input("Please enter the company that made your vehicle.")
        self.model = input("Please enter your vehicles model.")
        self.doors = input("Please enter whether your vehicle has 2 or 4 doors.")
        # Since the assignment wanted 2 or 4 doors I made a while loop to check if it's 2 or 4
        while self.doors != 2 or 4:
            print("Please enter either 2 or 4")
            self.doors = input("Please enter whether your vehicle has 2 or 4 doors.")
            if self.doors == 2 or 4:
                break
        self.roof = input("Please enter either solid or sun for the type of roof your vehicle has.")
        # Similar to the amount of doors the assignment wanted to check if the vehicle had a solid or sun roof so I made this while loop
        while self.roof != 'solid' or 'sun':
            print("Please enter either solid or sun")
            self.roof = input("Please enter either solid or sun for the type of roof your vehicle has.")
            if self.roof == 'solid' or 'sun':
                break

    # defining various functions within the class to print the users input
    def user_car_year(self):
        print("Year:", self.year)
    
    def user_car_make(self):
        print("Make:", self.make)

    def user_car_model(self):
        print("Model:", self.model)

    def user_car_doors(self):
        print("Number of doors:", self.doors)
    
    def user_car_roof(self):
        print("Type of roof:", self.roof, 'roof')

# Calls on Automobile, which then asks the user for year, make, model, doors, and roof. Type or preset as per assignment instructions
# Prints the results in a nice clean way
user_year = Automobile('car')
user_year.user_vehicle_type()
user_year.user_car_year()
user_year.user_car_make()
user_year.user_car_model()
user_year.user_car_doors()
user_year.user_car_roof()