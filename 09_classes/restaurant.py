class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"the restaurant name is {self.restaurant_name}")
        print(f"the type of food is {self.cuisine_type}")
    
    def open_restaurant(self):
        print("we are open")

#new stuff
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'mint']

    def displayflavors(self):
        print(f'We currently have {self.flavors} as flavors')
