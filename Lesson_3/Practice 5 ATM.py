mins = [5,10,20,50]
maxs = [100,200,500]

while True:
    sum = int(input('Введите сумму  '))
    if sum < 5 or sum%5!=0:
        print('Сумма должна быть кратна 5 ')
        continue
    else:
        break

while sum>0:
    for i in sorted(mins, reverse = True):
        if sum//i>=10:
            print (i, '-', 10)
            sum=sum-(i*10)
        else:
            print (i, "-", sum//i)
            sum=sum-i*(sum//i)
    for i in sorted(maxs, reverse = True):
        print (i, '-', sum//i)
        sum=sum-i*(sum//i)


