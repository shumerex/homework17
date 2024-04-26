class Vehicle:
    def __init__(self):
        self.vehicle_type = "none"


class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.price = 1000000

    def horse_powers(self):
        return "Не указано количество лошадиных сил"


class Nissan(Car):
    def __init__(self):
        super().__init__()
        self.vehicle_type = "car"
        self.price = 1500000

    def horse_powers(self):
        return "300 лошадиных сил"


nissan_car = Nissan()
print(f"Тип транспортного средства: {nissan_car.vehicle_type}")
print(f'Цена автомобиля Nissan: {nissan_car.price}')