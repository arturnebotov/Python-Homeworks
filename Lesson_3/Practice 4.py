a = [1000,500,200,100,50]

while True:
    b = int(input("Enter the amount multiple fifty "))
    if b < 50:
        print("Invalid amount")
        continue
    if b%50!=0:
        print("Invalid amount")
        continue
    else:
        break

for i in a:
    if b // i:
        print(b // i, i)
        b = b - (b // i)*i
