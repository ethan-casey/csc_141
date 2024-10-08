def city_country(city, country):
    city_info = f"{city}, {country}"
    return city_info.title()

print(f"{city_country('santiago', 'chile')}")
print(f"{city_country('pyongyang', 'north korea')}")
print(f"{city_country('havana', 'cuba')}")