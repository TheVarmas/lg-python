# If the number is divisible by 2 and 3, then say it's divisible by 6
# If a number is divisible by 2 or 3, say mutiple of 2/3
#print('SyntaxError:Invalid syntax') 

#print("print('a')this is code")
#jjjjj hashes are green
#Print = "la" 

#print(Print)
upper_list = ['A' ,'B','C','D','E','F','G','H','I','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
lower_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
str1 = 'j'

if str1 in upper_list:
    print('uppercase')
elif str1 in lower_list: 
    print('lowercase') 
else:
    print(f'you entered {len(str1)} characters you should enter 1 and do not enter numbers and symbols')

# Greatest of 2 numbers
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))

if num1 > num2:
    print(f'{num1} is the greater than {num2}')
elif num1 < num2:
    print(f'{num2} is the greater than {num1}')
else:
    print('Both the numbers that you entered are the same')

# Greatest of 3 numbers using 'and'
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))
num3 = int(input('Enter one more number: '))

if num1 == num2 == num3:
    print('All the numbers are same')  
elif num1 >= num2 and num1 >= num3:
    print(f'{num1} is the greatest')
elif num2 >= num1 and num2 >= num3:
    print(f'{num2} is the greatest')
elif num3 >= num2 and num3 >= num1:
    print(f'{num3} is the greatest')

# Postive, negative or zero
num1 = float(input('Enter a number: '))

if num1 < 0:
    print(f'{num1} is a negative number')
elif num1 > 0:
    print(f'{num1} is a postive number')
else:
    print(f'{num1} is zero')

# Divisible by 5 and 11
num1 = float(input('Enter a number: '))

if num1 % 55 == 0:
    print(f'{num1} is divisible by 5 and 11')
else:
    print(f'{num1} is not divisible by 5 and 11')

# Input weekday number and print week day.
weekday_num = input("Enter a weekday number: ")

if weekday_num == '1':
    print('Sunday')
elif weekday_num == '2':
    print('Monday')
elif weekday_num == '3':
    print('Tuesday')
elif weekday_num == '4':
    print('Wednesday')
elif weekday_num == '5':
    print('Thursday')
elif weekday_num == '6':
    print('Friday')
elif weekday_num == '7':
    print('Saturday')
else:
    print('Invalid weekday number')

#Factorial
a = int(input('Enter a number to get the factorial: '))

#if ValueError:
#    print('I said enter a number')
factorial = a 

for i in range(a - 1, 0, - 1):
    factorial = factorial * i

print(f'The factorial of {a} is {factorial}')      

###################################

num = int(input('Enter a number: '))

result = 1
i = 1

while i <= num:
    result *= i
    i += 1

print(result)

#################### Sum of first n natural numbers
num = int(input('Enter a number: '))

result = 0
i = 1
answer = '1'

while i <= num:
    result += i
    i += 1

    if i <= num:
        answer = answer + f' + {i}'

print(f'{answer} = {result}')

######

num = int(input('Enter a number: '))
print(f'Sum of first {num} natural number is {int(num * (num + 1) / 2)}')

########################

num = int(input('Enter a number: '))

result = 0
i = 1

while i <= num:
    result += i
    i += 1

print(f'The sum of first {num} natural numbers is {result}')

################# Sum of even and odd numbers ################
# Initialization(s):
# 	i: 1
# 	even_sum: 0
# 	odd_sum: 0
# 	even_sum_counter: 2
# 	odd_sum_counter: 1
i = 1
even_sum = 0
odd_sum = 0
even_sum_counter = 2
odd_sum_counter = 1

# Condition(s):
# 	i <= 5
while i <= 5:
    # Calculations
    even_sum += even_sum_counter
    odd_sum += odd_sum_counter
	
    even_sum_counter += 2
    odd_sum_counter += 2

    i += 1

print(even_sum, odd_sum)	

##############################


a = 1
b = 1
c = a + b
i = 4
num = int(input('enter a number: '))
if num == 1 or num == 2:
    print(1)
else:    
    while i <= num:
        a = b
        b = c
        c = a + b
        i += 1
        print(c)    
     # Should print 10 5

#####################################

a = 0
b = 1
num = int(input('Enter a number: '))
if num == 1:
    print(1)
else:
    i = 2
    print(b)
    while i <= num:
        c = a + b
        a = b
        b = c
        i += 1
        print(c)

################################

num = int(input('Enter a number: '))
a = num 
num2 = int(input('Enter another number: '))

while a >= num2:
    print(a)
    a -= 1

###############################

num_str = input('Enter a 3-digit number: ')
d1c = int(num_str[0]) ** 3
d2c = int(num_str[1]) ** 3
d3c = int(num_str[2]) ** 3

dcs = d1c + d2c + d3c
num = int(num_str)

if dcs == num:
    print(f'{num} is an Armstrong number: {num} == {dcs}')
else:
    print(f'{num} is not an Armstrong number: {num} != {dcs}')

###########################################

rows = int(input('Enter a number: '))
columns = int(input('Enter another number: '))
i = 1
j = 1
k = 1
depths = int(input('Enter another number: '))
while i <= rows:
    while j <= columns:
        while k <= depths:
            print((i, j, k))
            k += 1
        j += 1
        k = 1
    i += 1    
    j = 1        

####################################

str1 = input('Enter a number: ')

if str1.isalpha():
    if len(str1) == 1:
        print(f'{str1} is an alphabet')
    else:
        print(f'{str1} exceeds 1 character limit')
else:
    print(f'{str1} is not an alphabet')

################################

# If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
# If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
# If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
# The year is a leap year (it has 366 days).
# The year is not a leap year (it has 365 days).

year = int(input('Enter a year: '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('[1] It is a leap year')
        else:
            print('[2] Not a leap year')
    else:
        print('[3] It is a leap year')
else:
    print('[4] Not a leap year')

####################################

while True:
    num_str1 = input('Enter a number: ')
        
    if num_str1.isnumeric():
        num = int(num_str1)
        break

while True:
    num_str2 = input('Enter a number 2: ')
        
    if num_str2.isnumeric():
        num = int(num_str2)
        break

while True:
    num_str3 = input('Enter a number 3: ')
        
    if num_str3.isnumeric():
        num = int(num_str3)
        break

while True:
    num_str4 = input('Enter a number 4: ')
        
    if num_str4.isnumeric():
        num = int(num_str4)
        break

while True:
    num_str5 = input('Enter a number 5: ')
        
    if num_str5.isnumeric():
        num = int(num_str5)
        break
##################################

from mydefs import is_pali
string = input('Enter a sentence: ')

print(is_pali(string))
###########################################