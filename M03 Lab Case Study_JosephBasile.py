class Vehicle():
    def __init__(self, type):
        self.type = 'car'
    
    def user_vehicle_type(self):
        print("Vehicle Type:", self.type)
    

class Automobile(Vehicle):
    def __init__(self, type):
        super().__init__(type)
        self.year = input("Please enter the year your car was made.")
        self.make = input("Please enter the company that made your vehicle.")
        self.model = input("Please enter your vehicles model.")
        self.doors = input("Please enter whether your vehicle has 2 or 4 doors.")
        while self.doors != 2 or 4:
            print("Please enter either 2 or 4")
            self.doors = input("Please enter whether your vehicle has 2 or 4 doors.")
            if self.doors == 2 or 4:
                break
        self.roof = input("Please enter either solid or sun for the type of roof your vehicle has.")
        while self.roof != 'solid' or 'sun':
            print("Please enter either solid or sun")
            self.roof = input("Please enter either solid or sun for the type of roof your vehicle has.")
            if self.roof == 'solid' or 'sun':
                break
    
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

user_year = Automobile('car')
user_year.user_vehicle_type()
user_year.user_car_year()
user_year.user_car_make()
user_year.user_car_model()
user_year.user_car_doors()
user_year.user_car_roof()