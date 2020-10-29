from mydefs import get_primes_and_composites, ask_for_num
def get_primes_and_composites_dict():
    num1 = ask_for_num()
    num2 = ask_for_num()
    result = get_primes_and_composites(num1, num2)
    primes = result[0]
    composites = result[1]
    #print(f'primes:{primes}')
    #print(f'composites:{composites}')

<<<<<<< HEAD
    #foo = ([], [])
    ID = {'primes_list':primes,
    'composites_list':composites            }
    return ID

print(get_primes_and_composites_dict())      
=======
num1 = ask_for_num()
num2 = ask_for_num('Enter another one: ')
print(get_primes_and_composites(num1, num2))
>>>>>>> 37204bfbaf56d3d6e3d7f6ad3674f7721ad20949
