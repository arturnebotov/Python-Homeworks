sum = int(input('Введите сумму  '))
nominals = [5, 10, 20, 50, 100, 200, 500]

if sum < 5:
    print('Не допустимая сумма')
if sum > 5000:
    print("К сожалению банкомат не может выдать такую сумму")

while sum:
    for i in nominals:
        if 10 >=sum / i >= 1:
            print(i, " - ", sum // i)  # // целочисленное деление
            sum = sum % i







