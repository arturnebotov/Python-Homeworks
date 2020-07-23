f1 = open('D:\\Python A-level ext4\\Lesson 3\\20 lines.txt', 'r') # чтение
f2 = open('D:\\Python A-level ext4\\Lesson 3\\Result task 2 homework .txt', 'w') #запись
for line in f1.readlines():
	arr = line.split(" ")
	f2.write(line)
	for i in range(1, int(arr[2])+1):
		a = ''
		if (i % int(arr[0]) == 0):
			a += 'F'
		if (i % int(arr[1]) == 0):
			a += 'B'
		if a == '':
			a += str(i)
		f2.write(a + ' ')
	f2.write('\n\n')
f1.close()
f2.close()