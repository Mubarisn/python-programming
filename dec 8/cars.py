class Car:
    def __init__(self,color,price,kilometer):
        self.color=color
        self.price=price
        self.kilometer=kilometer


    def compare_price(self,other_car):
        if self.price > other_car.price:
            return f"{self.color} car is expensive than {other_car.color} car."
        elif self.price < other_car.price:
            return f"{other_car.color} car is expensive tahn {sef.color}car."
        else:
            return "both cars have same price."

    def add_kilometer(self,other_car):
        total_kilometers = self.kilometer + other_car.kilometer
        return f"the total kilometers of the two cars is {total_kilometers} km."

car1 = Car("Red",873678,2000)
car2 = Car("blue",45656,3000)

print(car1.compare_price(car2))
print(car1.add_kilometer(car2))
