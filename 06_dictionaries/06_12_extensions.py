"""
alex = {'first_name': 'Alex', 'last_name': 'DeNardo',
         'age': 20, 'city': 'somewhere'}
neel = {'first_name': 'Neel', 'last_name': 'Lynch',
         'age': 20, 'city': 'somewhere'}
the_hatman = {'first_name': 'The', 'last_name': 'Hatman',
         'age': '???', 'city': 'somewhere'}
names = [alex, neel, the_hatman]
for name in names:
    print(f"{name}")

This is the code from #7
"""

names = {
        'alex': {
            'first_name': 'Alex',
            'last_name': 'DeNardo',
            'age': '20',
            'city': 'somewhere'
        },
        'neel': {
            'first_name': 'Neel',
            'last_name': 'Lynch',
            'age': '19',
            'city': 'somewhere'
        },
        'the_hatman': {
            'first_name': 'The',
            'last_name': 'Hatman',
            'age': '???',
            'city': '???'
        }
    }
for people, name_info in names.items():
    print(f"Name: {people.title()}")
    full = f"{name_info['first_name']} {name_info['last_name']}"
    age = f"{name_info['age']}"
    city = f"{name_info['city']}"
    print(f"Full Name: {full}")
    print(f"Age: {age}")
    print(f"city: {city}\n")