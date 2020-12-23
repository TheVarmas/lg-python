import random
from mydefs import ask_for_num

frm = ask_for_num("Asking a question: ")
to = ask_for_num("Asking another question:  ")
answer = random.randint(frm, to)

print(answer)

guess = ask_for_num(f'What is the number({frm}, {to}):  ')


if guess > answer:
    print("Go lower!")
elif guess < answer:
    print("Go higher!")  
else:
    print("You got it!") 

