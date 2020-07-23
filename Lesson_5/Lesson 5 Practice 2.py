import math
a = [2,3,5,16,31,7,14,23,15,35,33,53,7,41,80,10,61,27]

def func (x):
    return x ** 2

result = list(map(lambda x:func(x) if (math.factorial(x-1)+1)%x==0 else False, a))
print(result)