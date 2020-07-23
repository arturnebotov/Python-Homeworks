a = list(range(1, 4))

def is_prime(proverka):
    d = 2
    while proverka % d:
        d += 1
    return d == proverka

def kvadrat(numb):
    if is_prime(numb):
        return numb**2
    return numb

print(list(map(kvadrat, a)))



