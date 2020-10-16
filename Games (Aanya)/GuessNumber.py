import random

frm = 1
to = 10
entered = int(input('Guess what I am thinking from 1 to 10 in 1 guess: '))

rr = random.randint(frm, to)

tries = 1
while entered != rr:
    tries += 1
  
    if entered > to or entered < frm:
        print(f'Guess between {frm} to {to}')
  
    entered = int(input('Try again: '))

print(f"You got it in {tries} tries")