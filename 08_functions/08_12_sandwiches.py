def make_sandwich(*toppings):
    print("\nMaking sandwich with these ingredients:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('cheese')
make_sandwich('lettuce', 'mayo')
make_sandwich('cheese', 'more cheese', 'even more cheese')

