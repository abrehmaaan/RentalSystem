class RentalShop:
    def __init__(self):
        self.inventory = {
            'hatchback': 10,
            'sedan': 5,
            'suv': 3
        }
        self.prices = {
            'hatchback_short': 30,
            'sedan_short': 50,
            'suv_short': 100,
            'hatchback_long': 25,
            'sedan_long': 40,
            'suv_long': 90
        }

    def display_inventory(self):
        print("Current inventory:")
        for car_type, count in self.inventory.items():
            print(f"{car_type}: {count}")

    def display_prices(self):
        print("Current prices:")
        print("Hatchback (per day):")
        print(f"Less than a week: ${self.prices['hatchback_short']}")
        print(f"More than a week: ${self.prices['hatchback_long']}")
        print("Sedan (per day):")
        print(f"Less than a week: ${self.prices['sedan_short']}")
        print(f"More than a week: ${self.prices['sedan_long']}")
        print("SUV (per day):")
        print(f"Less than a week: ${self.prices['suv_short']}")
        print(f"More than a week: ${self.prices['suv_long']}")

    def rent_car(self, car_type, duration):
        if self.inventory[car_type] == 0:
            print("Sorry, that car is not available.")
            return
        if duration < 7:
            price = self.prices[car_type + '_short']
        else:
            price = self.prices[car_type + '_long']
        total_price = price * duration
        self.inventory[car_type] -= 1
        return price, total_price

    def return_car(self, car_type):
        self.inventory[car_type] += 1
        print(f"Thank you for returning the {car_type} car.")

    def issue_bill(self, car_type, duration, total_price):
        print("Here is your bill:")
        print(f"Type of car: {car_type}")
        print(f"Duration of rental: {duration} days")
        print(f"Total payment: ${total_price}")