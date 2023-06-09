# Задание:
# https://i.gyazo.com/f039fb08568237d4ba9900ae47a089f3.png

# Решение:
def format_name_list(names):
    s = ''
    for i in names:
        if len(names) == 1:
            s += i["name"]
        elif i == names[-1]:
            s += "и " + i["name"]
        elif i == names[-2]:
            s += i["name"] + " "
        else:
            s += i["name"] + ", "
    return s

# код ниже не стоит удалять, он нужен для проверки
assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}, {'name': 'Homer'}, {'name': 'Marge'}]) == 'Bart, Lisa, Maggie, Homer и Marge'
assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'}]) == 'Bart, Lisa и Maggie'
assert format_name_list([{'name': 'Bart'}, {'name': 'Lisa'}]) == 'Bart и Lisa'
assert format_name_list([{'name': 'Bart'}]) == 'Bart'
assert format_name_list([]) == ''
assert format_name_list([{'name': 'Maggie'}, {'name': 'Lisa'}, {'name': 'Barney'}, {'name': 'Homer'}, {'name': 'Bart'}, {'name': 'Moe'}]) == 'Maggie, Lisa, Barney, Homer, Bart и Moe'
assert format_name_list([{'name': 'Marge'}, {'name': 'Maggie'}, {'name': 'Seymour'}]) == 'Marge, Maggie и Seymour'
assert format_name_list([{'name': 'Maude'}, {'name': 'Bart'}]) == 'Maude и Bart'
print('Проверки пройдены')