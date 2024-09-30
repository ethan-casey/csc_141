favorite_places = {
                'alex': {
                    'first': 'france',
                    'second': 'texas',
                    'third': 'home'
                },
                'sam': 'school',
                'ethan': {
                    'first': 'bedroom',
                    'second': 'basement'
                }
    }
for place, favorite_place in favorite_places.items():
    print(f"\nPerson: {place}")
    print(f"likes to go to {favorite_place}")