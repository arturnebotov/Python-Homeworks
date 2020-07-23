while True:
    Fizz = int(input('Please enter the first number  '))
    Buzz = int(input('Please enter the second number  '))
    N = int(input('Please enter the third number  '))
    if N <1 or Fizz < 1 or Buzz < 1:
        print("All your numbers should be positive. Please enter another numbers")
        continue
    else:
        break


for i in range(1,N+1):
    a = ''
    if (i % int(Fizz) == 0):           # % = остаток от деления
        a += 'F'
    if (i % int(Buzz)== 0):
        a += 'B'
    if a=='':
        a += str(i)
    print (a, end = " ")