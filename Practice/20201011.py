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
