def car_profile(manufacturer, model_name, **car_info):
    car_info['manufacturer_name'] = manufacturer
    car_info['model_name'] = model_name
    return car_info

car_stuff = car_profile('subaru', 'outback',
                  color='blue',
                  tow_package='True')

print(car_stuff)