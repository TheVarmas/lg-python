cars = {'grey':['car1'], 'blue':['car2', 'car3']}

color = input('Enter a color: ')

car_values = cars.get(color.lower(), []) # cars[color]

if len(car_values) == 1:
    print(f"{car_values} is {color}")
elif len(car_values) > 1:
    print(f"{car_values} are {color}")
else:
    print(f"No cars found with the color {color}")
