rivers = {'nile': 'egypt', 
          'missisipi': 'north america',
          'amazon': 'brazil'}
for names, country in rivers.items():
    print(f"The {names} run through {country}")
for value in rivers.values():
    print(f"{value}")