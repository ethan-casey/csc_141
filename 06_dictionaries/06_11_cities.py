cities = {
            'new_york_city': {
                 'country': 'new_york',
                'population':'8.8 million',
                'fact': "world's largest subway"
                },
            'los angeles': {
                'country': 'california',
                'population': '3.9 million',
                'fact': 'entertainment capital of the world'
                },
            'chicago': {
                'country': 'illinois',
                'population': '2.6 million',
                'fact': 'third largest city'
                }
            }
for name, city_info, in cities.items():
    print(f"\nName: {name}")
    country = f"the country it is in is {city_info['country']}"
    population = f"the population is {city_info['population']}"
    fact = f"a random fact is that it is the {city_info['fact']}"
    print(country)
    print(population)
    print(fact)