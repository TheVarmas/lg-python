from mydefs import ask_for_num
print('1. Factorial')
print('2. Sum')
choice = ask_for_num('Enter your choice: ')
if choice == 2:
    n = ask_for_num()
    result = 0
    for i in range(1, n + 1):
        result += i
    print(result)
elif choice == 1:
    o = ask_for_num()
    factorial = 1
    for j in range(1, o + 1):
            factorial = factorial * j
    print(factorial)
else:
    print(f'{choice} is not a valid choice')    