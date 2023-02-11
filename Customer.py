class Customer:
    def __init__(self, rental_shop):
        self.rental_shop = rental_shop
        self.rented_car = None
        self.rented_car_type = None
        self.rented_duration = None
        self.total_price = None

    def inquire_inventory(self):
        self.rental_shop.display_inventory()

    def inquire_prices(self):
        self.rental_shop.display_prices()

    def rent_car(self, car_type, duration):
        self.rental_shop.rent_car(car_type, duration)
        self.rented_car = True
        self.rented_car_type = car_type
        self.rented_duration = duration
        if duration < 7:
            price = self.rental_shop.prices[car_type + '_short']
        else:
            price = self.rental_shop.prices[car_type + '_long']
        self.total_price = price * duration
        return price, self.total_price

    def return_car(self):
        if self.rented_car:
            self.rental_shop.return_car(self.rented_car_type)
            self.rental_shop.issue_bill(self.rented_car_type, self.rented_duration, self.total_price)
            self.rented_car = None
            self.rented_car_type = None
            self.rented_duration = None
            self.total_price = None
        else:
            print("You do not have a car rented.")
