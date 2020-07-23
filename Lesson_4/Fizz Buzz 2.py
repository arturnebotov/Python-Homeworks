while True:
    Fizz = int(input('Please enter the first number  '))
    Buzz = int(input('Please enter the second number  '))
    N = int(input('Please enter the third number  '))
    if N <1 or Fizz < 1 or Buzz < 1:
        print("All your numbers should be positive. Please enter another numbers")
        continue
    else:
        break

c = []
c = ['FB' if (i % int(Fizz) == 0 and i % int(Buzz)== 0) else 'F' if i % int(Fizz) == 0 else 'B' if i % int(Buzz)== 0
else str(i) if i=='' else i for i in range(1,N+1)]
print(c)

