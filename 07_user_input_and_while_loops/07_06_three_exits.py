toppings = "\nwhat kind of toppings do you want on your pizza?:\n"
toppings += "Enter 'quit' to stop the program. "

while True:
    message = input(toppings)

    if message == 'quit':
        break
    else:
        print(f"I will put {message} on your pizza")
#this already meets the requirements so i didn't change it