sandwich_orders = ['tuna sandwich', 'cheese sandwich', 'turkey sandwich',
                   'pastrami sandwich', 'pastrami sandwich', 'pastrami sandwich']
print("we have no more pastrami")

finished_sandwiches = []

while 'pastrami sandwich' in sandwich_orders:
    sandwich_orders.remove('pastrami sandwich')

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"currently making the {current_sandwich}")
    finished_sandwiches.append(current_sandwich)
print(f"\nI have finished making these:")
for sandwich_list in finished_sandwiches:
    print(sandwich_list)