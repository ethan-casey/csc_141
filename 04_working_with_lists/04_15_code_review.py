foods = ('sandwich', 'fries', 
         'salad', 'curry', 'burger')
for food in foods:
    print(food)
foods[0] = "carrot"
foods = ('carrot', 'fries',
          'taco', 'curry', 'burger')
for food in foods:
    print(food)

my_foods = ['pizza', 'falafel', 'carrot cake']
friends_foods = my_foods[:]
for foods in my_foods:
    print(foods) 
for friendfood in friends_foods:
    print(friendfood)

threes = []
for value in range(1, 11):
    three = value * 3
    threes.append(three)
print(threes)
print("the first three litems in my list are:")
print(threes[0:3])
print("three items from the middle of my list are:")
print(threes[3:6])
print("the last three items in my list are:")
print(threes[-3:])