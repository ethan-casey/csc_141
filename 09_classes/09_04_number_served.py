class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        #adding number served attribute
        self.number_served = 0

    def describe_restaurant(self):
        print(f"the restaurant name is {self.restaurant_name}")
        print(f"the type of food is {self.cuisine_type}")
    
    def open_restaurant(self):
        print("we are open")

    #modifying through method
    def set_number_served(self, served):
        self.number_served = served

    #increment method
    def increment_number_served(self, serviced):
        self.number_served += serviced

my_restaurant = Restaurant("Big Pete's House of Munch", 'Fast Food')
print(f"{my_restaurant.restaurant_name}")
print(f"{my_restaurant.cuisine_type}")
my_restaurant.describe_restaurant()
my_restaurant.open_restaurant()

#prints number served
restaurant = Restaurant('munch house', 'good food')
print(f"{restaurant.number_served}")

#method modify
restaurant.set_number_served(4)
print(f"{restaurant.number_served}")

#increment method
restaurant.increment_number_served(20)
print(f"{restaurant.number_served}")