class User:
    def __init__(self, first_name, last_name, age, state):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.state = state
        #login attempt attribute
        self.login_attempts = 0

    def describe_user(self):
        print("Information:")
        print(f"name: {self.first_name} {self.last_name}, age: {self.age}, state: {self.state}")

    def greet_user(self):
        print(f"Hello {self.first_name}")
    
    #increment login attempts
    def increment_login_attempts(self):
        self.login_attempts += 1

    #reset attempts
    def reset_login_attempts(self):
        self.login_attempts = 0

#testing
user = User('Ethan', 'Casey', 20, 'PA')
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"{user.login_attempts}")
user.reset_login_attempts()
print(f"{user.login_attempts}")