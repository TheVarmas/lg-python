from_str = input('Enter a number: ')
to_str = input('Up to? ')

from_num = int(from_str)
to_num = int(to_str)

i = from_num
while i <= to_num:
    j = 0
    sum_of_cubes = 0
    while j < len(str(i)):
        sum_of_cubes += int(str(i)[j]) ** 3
        j += 1
    if sum_of_cubes == i:
        print(f'{i} is an Armstrong number: {i} == {sum_of_cubes}')
    
    i += 1