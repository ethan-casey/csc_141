class User:
    def __init__(self, first_name, last_name, age, state):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.state = state

    def describe_user(self):
        print("Information:")
        print(f"name: {self.first_name} {self.last_name}, age: {self.age}, state: {self.state}")

    def greet_user(self):
        print(f"Hello {self.first_name}")

#new stuff
class Admin(User):
    def __init__(self, first_name, last_name, age, state):
        super().__init__(first_name, last_name, age, state)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(f"the admin can do these things: {self.privileges}")

#new stuff
my_admin = Admin('Ethan', 'Casey', 20, 'PA')
my_admin.show_privileges()