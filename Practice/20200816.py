import random 
frm = 1
to = 10
entered = int(input('guess what I am thinking from 1 to 10 in one guess: '))

rr = random.randint(frm, to)
print(rr)
#print('guess what I am thinking from 1 to ten in 1 guess')
if entered > to:
    print(f'guess beetween {frm} to {to}')
if entered == rr:
    print('you got it!')
else:
    print('oh no! you ran out of guesses!  ')    