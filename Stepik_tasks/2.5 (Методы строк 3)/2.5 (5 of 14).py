students = ['Ivan', 'Masha', 'Sasha']
#students.remove('Sasha')
#Результат ['Ivan', 'Masha']
#del students[0]
#['Masha']

if 'Ivan' in students:
    print('Ivan is here!')
if 'Ann' not in students:
    print('Ann is out')

ind = students.index('Sasha')
# Результат 2
ind = students.index('Ann')
# Результат: ValueError: 'Ann' is not in list