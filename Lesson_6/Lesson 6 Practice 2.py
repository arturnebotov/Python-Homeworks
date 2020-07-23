Python = {"Сидоров Иван", "Коваленко Михаил", "Куров Василий", "Иван Василиевич"}
FrontEnd = {"Лаврушкина Людмила", "Орешко Игорь", "Петров Николай", "Иван Василиевич"}
FullStack = {"Сидоров Иван", "Солнышкина Маша", "Кузякин Василий", "Иван Петрович"}
Java = {"Сидоров Иван", "Малышкин Михаил", "Баракин Василий", "Куров Василий"}



print('Students who study in more than two groups :', (Python&FullStack&FrontEnd&Java)|(Python&FullStack&FrontEnd)|(Python&FullStack&Java)|(FullStack&FrontEnd&Java)|
      (Python&FrontEnd&Java)|(Python&FrontEnd)|(Python&FullStack)|(Python&Java)|(FrontEnd&FullStack)|(FrontEnd&Java)|(FullStack&Java))

print('Students who do not study on the FrontEnd :',(Python | FullStack | Java) - FrontEnd)

print("Python students :", Python)




