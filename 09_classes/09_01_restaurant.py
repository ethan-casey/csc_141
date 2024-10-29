class restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"the restaurant name is {self.restaurant_name}")
        print(f"the type of food is {self.cuisine_type}")
    
    def open_restaurant(self):
        print("we are open")

my_restaurant = restaurant("Big Pete's House of Munch", 'Fast Food')
print(f"{my_restaurant.restaurant_name}")
print(f"{my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()