import random
from mydefs import ask_for_num

options = [1, 2, 3]
choices = ['Rock', 'paper', 'scissors']
computer_answer = random.randint(1,3)

print("Welcome to rock, paper, scissors!")
print(choices[computer_answer - 1])
for i in range(len(choices)):
    print(f'{options[i]}. {choices[i]}')

user_answer = ask_for_num("Pick an option:  ")

if user_answer == computer_answer:
    print(f"It is a draw!We both picked {choices[computer_answer - 1]}")
elif user_answer != computer_answer:
    print(f"The computer picked {choices[computer_answer - 1]} and you picked {choices[user_answer - 1]}")
#rr, pp, ss - Done
#p r - Done
#s p - Done
#r s 
#r p - Done
#p s - Done
#r s
if computer_answer == 2 and user_answer == 1:
    print('You lost: Paper beats Rock')
elif computer_answer == 1 and user_answer == 2:
    print("You won: Paper beats Rock")
elif computer_answer == 3 and user_answer == 2:
    print("You lost: Scissors beats Paper")
elif computer_answer == 2 and user_answer == 3:
    print("You won: Scissors beats Paper")
elif computer_answer == 1 and user_answer == 3:
    print("You lost: Rock beats Scissors")
elif computer_answer == 3 and user_answer == 1:
    print("You won: Rock beats Scissors")