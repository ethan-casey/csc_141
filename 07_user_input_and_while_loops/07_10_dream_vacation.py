responses = {}
polling_active = True
while polling_active:
    name = input("\nwhat is your name?: ")
    response = input("if you could visit one place in the world, where would you go?: ")

    responses[name] = response

    repeat = input("Would you like to take the poll again? (y/n): ")
    if repeat == 'n':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to go to {response}")