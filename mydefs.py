def ask_for_num(message='Enter a number: '):
    while True:
        num_str = input(message)
            
        if num_str.isnumeric():
            return int(num_str)

def get_factorial(num):
    result = 1
    i = 1

    while i <= num:
        result *= i
        i += 1

    return result

#######################################==
def is_even(num):
    return num % 2 == 0
#===============================++++++++++++=====
def double_of_num(num):
    return num * 2
#=============================================
def is_pali(sentence):
    sentence_reverse = sentence.lower()[::-1]
    return sentence.lower() == sentence_reverse
        
#==================================================
def is_prime(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:        
            return False
    return True
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def get_primes(start, end):
    nums = []
    for i in range(start, end + 1):
        if is_prime(i):
            nums.append(i)
    return nums
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def get_primes_and_composites(frm, to):
    primes = []
    composites = []
    for i in range(frm, to + 1):
        if is_prime(i):
            primes.append(i)
        else:
            composites.append(i)
    return primes, composites        