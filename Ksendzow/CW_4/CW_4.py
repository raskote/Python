# Tuple

# Тюпл
# person1 = ("Anna", 30)
# Список/Массив
# person2 = ["Anna", 30]
# Дикт
# person3 = {"Anna": 30}
# Сет/Множество
# person4 = {"Anna", 30}
# Фрозен сет
# person5 = frozenset({"Anna", 30})
# print("person1", person1, type(person1))
# print("person2", person2, type(person2))
# print("person3", person3, type(person3))
# print("person4", person4, type(person4))
# print("person5", person5, type(person5))

# person11 = ["Anna", 30, "QA"]
# person111 = tuple(person11)

# print(person11, type(person11), len(person111))
# print(person111, type(person111), len(person111))

# user = ("Anna", 30, "QA", "ITX", "Female")
# # name, age, position = user
# print(user[1:3])
#
# def get_user():
#     name = "Anna"
#     age = 30
#     position = "QA"
#
#     return name, age, position
#
# user = get_user()
# user2 = list(get_user())
# # user22 = user2.append("Mercedes")
# # user1[2] = "Mercedes"
#
#
# print(user)
# print(type(user))

# Итерация tuple
# for item in user:
#     print(item)
#
# position = "QA"
# if position in user:
#     print("OK")
# else:
#     print("NOT")

users = {1: "Alex",
         2: "Anna",
         3: "Ivan"}

users_list = [
    [1, "Alex"],
    [2, "Anna"],
    [3, "Ivan"]
]

users_json = dict(users_list)

# print('users - ', users, type(users))
# print('users_list - ', users_list, type(users))
# print('users = ', users_json, type(users))

#
# users = {1: "Alex",
#          2: "Anna",
#          3: "Ivan"}
#
# users_keys = {"item1": "Alex",
#               "item2": "Anna",
#               "item3": "Ivan"}

# key = 2
# user = users.pop(key)
# print(user, type(user))
# print(users)

# Распаковка дикта
# users_items = [value for value in users_keys.values()]
# print(users_items)
# print(users)
# users[2] = "Alexandra"
# print(users)

# users = {"Alex", "Anna", "Elena", "Sergey", "Anna", 1, 1, 1, 1, 1, 1}
# users_set = set(users)
# users_set.add("Maria")
# print(users)
# print(users_set)
#
# if "Elena" in users:
#     users.remove("Elena")
# print(users)




users1 = {"Elena", 1, "Anna", "Alex", "Elena"}
users2 = ["Mila", 2, "Natalia", "Oksana", 1, "Elena"]
print(users1)
print(users2)
users3 = users1.intersection(users2)
print(users3)