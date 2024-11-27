class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def car_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

    def start(self):
        print("The car is starting")

    def stop(self):
        print("The car is stopping")

# Create an object
my_car = Car("Toyota", "Camry", 2020)
my_car.car_info()
my_car.start()
my_car.stop()
