favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'rust',
                      'phil': 'python'}
people = ['alex', 'jen', 'neel', 'phil']
name = favorite_languages.keys()
for peps in people:
    if peps in name:
        print(f"thanks for taking the survey {peps}")
    else:
        print(f"take my survey {peps}")