#**PYTHON. HOMEWORK_1**
#1.	Создать переменную типа String
x1 = str("Kek")
#2.	Создать переменную типа Integer
x2 = int(1)
#3.	Создать переменную типа Float
x3 = float(5.5)
#4.	Создать переменную типа Bytes
x4 = bytes(10)
#5.	Создать переменную типа List
x5 = [1,2,3,4]
#6.	Создать переменную типа Tuple
x6 = (1,2,3)
#7.	Создать переменную типа Set
x7 = {"Ivan", "Rinat", "Olga", "Kira"}
#8.	Создать переменную типа Frozen set
x8 = frozenset(x7)
#9.	Создать переменную типа Dict
x9 = {'dict': 1, 'dictionary': 2}
#10.	Вывести в консоль все выше перечисленные переменные с добавлением типа данных.
print(x1, type(x1))
print(x2, type(x2))
print(x3, type(x3))
print(x4, type(x4))
print(x5, type(x5))
print(x6, type(x6))
print(x7, type(x7))
print(x8, type(x8))
print(x9, type(x9))
#11.	Создать 2 переменные String, создать переменную в которой сканкатенируете эти переменные. Вывести в консоль.
x = 'kek'
y = 'cheburek'
print(x+y)
#12.	Вывести в одну строку переменные типа String и Integer используя “,” (Запятую)
x = 'kek'
y = int(101)
print(x,y)
#13.	Вывести в одну строку переменные типа String и Integer используя “+” (Плюс)
x = 'kek'
y = int(101)
print(x+str(y))
