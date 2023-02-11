from RentalShop import RentalShop
from Customer import Customer
from VIP import VIP

# Create an instance of the RentalShop class
rental_shop = RentalShop()

# Set the initial inventory
rental_shop.inventory = {
    'hatchback': 4,
    'sedan': 3,
    'suv': 3
}

# Ask the user if they are a VIP member
vip_member = input("Are you a VIP member (Y/N)? ")

# Create an instance of the Customer or VIP class based on the user's response
if vip_member.lower() == 'y':
    customer = VIP(rental_shop)
else:
    customer = Customer(rental_shop)

# Ask the user what type of car they want to rent
car_type = input("What type of car do you want to rent (Hatchback, Sedan, SUV)? ").lower()

# Ask the user how long they want to rent the car
duration = int(input("How long do you want to rent this car (in days)? "))

# Rent the car for the specified duration
price, total_price = customer.rent_car(car_type, duration)
print(f"You have rented a {car_type} car for {duration} days.")
print(f"You will be charged ${price} per day, for a total of ${total_price}.")
print("We hope you enjoy our service!")

# Display the updated inventory
rental_shop.display_inventory()

# Ask the user if they want to return the car
return_car = input("Do you want to return the car (Y/N)? ")

# Return the car if the user responds 'Y'
if return_car.lower() == 'y':
    customer.return_car()
    # Display the updated inventory
    rental_shop.display_inventory()
