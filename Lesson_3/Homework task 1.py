f = open('D:\\Python A-level ext4\\Lesson 3\\20 lines.txt', 'r')
for line in f.readlines():                  #readlines() - построчное чтение из файла
	arr = line.split(" ")                   #с помощью split создаю из строки список, в скобках указан разграничитель
	print(line)
	for i in range(1, int(arr[2])+1):       #третий элемент в списке(индекс 2)
		a = ''
		if (i % int(arr[0]) == 0):          #первый элемент в списке(индекс 0)
			a += 'F'
		if (i % int(arr[1]) == 0):          #второй элемент в списке(индекс 1)
			a += 'B'
		if a == '':
			a += str(i)
		print(a, end=" ")
	print('\n')
f.close()
