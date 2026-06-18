class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def print_car_info(self):
        print(f"Марка: {self.brand}, Модель: {self.model}, Год: {self.year}")

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("BMW", "X5", 2022)
car3 = Car("Tesla", "Model 3", 2023)

car1.print_car_info()
car2.print_car_info()
car3.print_car_info()