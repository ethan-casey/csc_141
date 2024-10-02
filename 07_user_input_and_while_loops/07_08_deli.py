sandwich_orders = ['tuna sandwich', 'cheese sandwich', 'turkey sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"currently making the {current_sandwich}")
    finished_sandwiches.append(current_sandwich)
print(f"\nI have finished making these:")
for sandwich_list in finished_sandwiches:
    print(sandwich_list)