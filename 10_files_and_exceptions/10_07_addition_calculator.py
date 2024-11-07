print("I will add two numbers")
print("enter 'stop' to quit")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'stop':
        break
    second_number = input("Second Number: ")
    if second_number == 'stop':
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("You need numbers not letters")
    else:
        print(answer)