from getpass import getpass

users = [
    {
        'username': 'lightgoddess',
        'password': 'password1',
        'full_name': 'Aanya Varma Amaravati'
    },
    {
        'username': 'rockgod',
        'password': 'password2',
        'full_name': 'Kiran Kumar Varma Amaravati'
    },
    {
        'username': 'rockgoddess',
        'password': 'password3',
        'full_name': 'Usha Rani Amaravati'
    }
]

username_input = input('Enter a username: ')
password_input = getpass('Password: ')

user_found = False
for user in users:
    if username_input.lower() == user['username'].lower():
        if password_input == user['password']:
            print('You are logged in')
            user_found = True
            break

if user_found == False:
    print('Invalid credentials')

if user_found == True:  
    from mydefs import ask_for_num
    while 1 == 1:
        print('1.Addition')
        print('2.Subtraction')
        print('3.Multiplication')
        print('4.Division')
        print('5.Quit')

        choice = ask_for_num('Enter your choice [1-5]: ')
        if choice == 1:
            num1 = ask_for_num('Enter a number to add: ')
            num2 = ask_for_num(f'Enter  number to add to {num1}: ')
            print(f'{num1} + {num2} = {num1 + num2}')
        elif choice == 2:
            num1 = ask_for_num('enter a number to subtract from: ')
            num2 = ask_for_num(f'Enter a number to subtract from {num1}: ')
            print(f'{num1} - {num2} = {num1 - num2}')
        elif choice == 3:
            num1 = ask_for_num('enter a number to multiply:  ')
            num2 = ask_for_num(f'enter a number to multiply with {num1}:  ')
            print(f'{num1} x {num2} = {num1 * num2}')
        elif choice == 4:
            num1 = ask_for_num('enter a number: ')
            num2 = ask_for_num(f'Enter a number to divide with {num1}: ')
            print(f'{num1}/{num2} = {num1 / num2}')
        elif choice == 5:
            print('Bye!')
            break
        else:
            print('Invalid choice')    