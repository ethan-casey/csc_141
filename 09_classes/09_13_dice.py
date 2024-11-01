from random import randint

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return randint(1, self.sides)
    
d6 = Die()
results = []
for roll_num in range(10):
    result = d6.roll_die()
    results.append(result)
print(results)

#ten sided die
d10 = Die(sides=10)

results = []
for roll_num in range(10):
    result = d10.roll_die()
    results.append(result)
print(results)

#20 sided die
d20 = Die(sides=20)

results = []
for roll_num in range(10):
    result = d20.roll_die()
    results.append(result)
print(results)
