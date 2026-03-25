def car_make(manufacturer, model, **car_info):

     car_info['manufacturer'] = manufacturer
     car_info['model'] = model
     return car_info

car_profile = car_make('Isuzu', 'D-Max', color='Blue', Farm_Rigged=True)

for key, value in car_profile.items():
     print(f'{key.replace('_', ' ').title()}: {value}')