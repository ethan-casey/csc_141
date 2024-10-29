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

first_user = User('Ethan', 'Casey', 20, 'PA')
second_user = User('Alex', 'DeNardo', 20, 'PA')
first_user.describe_user()
first_user.greet_user()
second_user.describe_user()
second_user.greet_user()