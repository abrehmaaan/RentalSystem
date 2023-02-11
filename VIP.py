from Customer import Customer
class VIP(Customer):
    def __init__(self, rental_shop):
        super().__init__(rental_shop)
        self.vip_prices = {
            'hatchback_short': 20,
            'sedan_short': 35,
            'suv_short': 80,
            'hatchback_long': 20,
            'sedan_long': 35,
            'suv_long': 80
        }

    def rent_car(self, car_type, duration):
        super().rent_car(car_type, duration)
        if duration < 7:
            price = self.vip_prices[car_type + '_short']
        else:
            price = self.vip_prices[car_type + '_long']
        self.total_price = price * duration
        return price, self.total_price
