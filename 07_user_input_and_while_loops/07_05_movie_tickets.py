current_age = "How old are you?: "

for price in current_age:
    price = input(current_age)
    price = int(price)
    if price < 3:
        print("your ticket is free!")
    elif price <= 12:
        print("your ticket is $10")
    else:
        print("your ticket is $15")