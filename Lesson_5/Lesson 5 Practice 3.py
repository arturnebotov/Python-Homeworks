f = open('Text.txt', 'r')
f = f.read()
f = f.split(' ')
dct = {}

for i in f:
    if i in dct:
        dct[i] += 1
    else:
        dct[i] = 1

for i in sorted(dct):
    print(i,':',dct[i])




