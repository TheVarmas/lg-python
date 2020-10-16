shoes = {'blue':2, 'green':0, 'red':5, 'yellow':1, 'violet':'?'}
shoes['white'] = 10
shoes['blue'] -= 1

key = input('Enter a shoe color: ')

if key in shoes:
    print(shoes[key])
else:
    print(f'There aren\'t any {key} shoes')

# input month number and print number of days in that month.
# Level 1: Fails on mixed case input

months = {'January':31, 'February':28, 'March':31, 'April':30,
'May':31, 'June':30, 'July':31, 'August':31, 'September':30,
'October': 31, 'November': 30, 'December': 31}

input_month = input('Enter a month: ')

if input_month in months:
    print(months[input_month])
else:
    print('Invalid month')

# input month number and print number of days in that month.
# Level 2: Preserves the input case and handles mixed case input gracefully

months = {'january':31, 'february':28, 'march':31, 'april':30,
'may':31, 'june':30, 'july':31, 'august':31, 'september':30,
'october': 31, 'november': 30, 'december': 31}

input_month = input('Enter a month: ')
if input_month.lower() in months:
    print(f'The number of days in {input_month} is {months[input_month.lower()]}')
else:
    print(f'{input_month} is an invalid month')
