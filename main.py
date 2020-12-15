import random
from mydefs import ask_for_num

options = [1, 2, 3]
choices = ['Rock', 'paper', 'scissors']
computer_answer = random.randint(1,3)



print("Welcome to rock, paper, scissors!")
print(computer_answer)
for i in range(len(choices)):
    print(f'{options[i]}. {choices[i]}')

user_answer = ask_for_num("Pick an option:  ")

if user_answer == computer_answer:
    print(f"It is a draw!We both picked {computer_answer}")