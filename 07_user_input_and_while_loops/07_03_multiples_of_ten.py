number = input("give me a number: ")
number = int(number)

if number % 10 == 0:
    print(f"{number} is divisable by ten")
else:
    print(f"{number} is not divisable by ten")