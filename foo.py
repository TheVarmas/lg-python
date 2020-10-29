from mydefs import get_primes_and_composites

def foo(*args, **kwargs):
    print(args)
    print(kwargs)
    #print(args[0] + args[4] + args[2])
foo(1, 2, 3, 4, 5, foo=1, bar=3)

print(get_primes_and_composites(frm=1, to=10))