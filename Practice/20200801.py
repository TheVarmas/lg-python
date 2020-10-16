# number >= 100 and if a number is even print 'large even number'
# number >= 100 and if a number is odd print 'large odd number'
# number < 100 and if a number is even print 'small even number'
# number < 100 and if a number is odd print 'small odd number'

num = 50

if num >= 100:
  if num % 2 == 0:
    print(f'{num} is a large even number')
  else:
    print(f'{num} is a large odd number')
else:
  if num % 2 == 0:
    print(f'{num} is a small even number')
  else:
    print(f'{num} is a small odd number')
