# TXT
folder_path = "C:/Users/delfile/PycharmProjects/Python/Ksendzow/CW_2/"
file_name = folder_path + '44_txt.txt'
dl = ["Anna", "Vadim", "Natalia", "Milana"]
# f = open(file_name, 'w')
#
# f.write('Hello world\n')
# f.write('Hello world\n')
# f.write('Hello world\n')
# f.write('Hello world\n')
# f.write('Hello world\n')
#
# f.close()

# with open(file_name, 'w', encoding='utf-8') as f:
    # f.write('Hi world')
    # f.writelines(dl)
    # f.write("\n".join(dl))

    # for line in dl:
    #     f.writelines(line) #(write) тоже отработает
    #     f.write('\n')

# with open(file_name, 'a') as f:
#     f.write("Hi World\n")

# with open(file_name, 'r') as f:
#     # ff = f.read()
#     # ff = f.read(11)
#     ff = f.readlines()
#     for i in ff:
#
#         print(i.rstrip())

#=============================

#CSV
users_list = [
    ['Vadim', 33],
    ['Alex', 32],
    ['Anna', 30]
]
import csv
csv_file_name = folder_path + '55_csv.csv'
# with open(csv_file_name, 'w') as csv_f:
#     writer = csv.writer(csv_f)
#     row = ["Alex", 32]
#     writer.writerow(row)
# Добавление строчек из заготовленного списка
# with open(csv_file_name, 'a') as csv_f:
#     writer = csv.writer(csv_f)
#     writer.writerows(users_list)

# Чтение таблицы
# with open(csv_file_name, 'r') as csv_f:
#     reader = csv.reader(csv_f)
#     for row in reader:
#         print(row)

# Запихать созданный заранее список в таблицу с только что созданными колонками
users = [
    {"name": "Vadim", "age": 32},
    {"name": "Anna", "age": 20},
    {"name": "Alex", "age": 25},
    {"name": "Elena", "age": 18}
]
# with open(csv_file_name, 'w') as csv_f:
#     columns = ["name", "age"]
#     writer = csv.DictWriter(csv_f, fieldnames=columns)
#     writer.writeheader() #прописать названия столбов (первая строчка)
#     writer.writerows(users)

# Чтение таблицы
with open(csv_file_name, 'r') as csv_f:
    reader = csv.DictReader(csv_f)
    for row in reader:
        print(row['name'], row['age'])