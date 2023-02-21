# l1 = [1, 2, 3, 4, 5]
# print(type(l1))

# names = ["Anna", "Alex", "Vadim"]
# print(type(names))

# l1 = []
# l2 = list()

# l3 = [9, 3.14, "Text", True, [3, 2, 0], {'name':'Anna'}]

# item1 = 'Yolochka'
# print(item1[1])

# l4 = list(item1)
# print(l4)

# l5 = [3]
# l55 = l5 * 4
# print(l55)

users = ["Alex", "Yolochka", "Anna"]
# print(users[0])
# print(users[1])
# print(users[2])

# users[1] = "Victor"
# print(users)

# u1, u2, u3 = users
# print(u2)

# for user in users:
# print(user)
# print(len(users))
# i = 0
# while i < len(users):
#     print(users[i])
#     i += 1

# l1 = [1,2,3]
# l2 = [1,2,3]
#
# if l1 == l2:
#     print("1    ---    l1 == l2")
# else:
#     print("2    ---    l1 != l2")

users = ["Alex", "Yolochka", "Anna", "Yolochka", "Victor"]
# users.append(77)
# print(users)
#
# users.insert(1,78)
# print(users)
#
# # users.extend(["Elena","Vika"])
# # print(users)
#
# index_item = users.index("Yolochka")
# print(index_item)
#
# users_remove = users.pop(1)
# print(users)
# print(users)
# users.pop()
# print(users)
# users.clear()
# print(users)

# if "Victor" in users:
#     print("OK! Item in List")
# else:
#     print("item not in list")

# users1 = ["Alex", "Yolochka", "Anna", "Victor", "Vika", "Elena", "Vadim","Sergey","Dima","Inna"]
# del users1[1]
# print(users1)

# del users1[1:]
# print(users1)

# del users1[:3]
# print(users1)

# del users1[2:5]
# print(users1)

# del users1[::2]
# print(users1)

# items = [1, 6, 1, 3, 7, 3, 1, 3, 6, 8, 2, 3, 4, 6, 2]
# items.sort()
# print(items)
# items.reverse()
# print(items)
#
# users1 = ["Anna", "Alex", "Victor"]
# users2 = users1
# users2.append("Elena")
# print(users1)
# print(users2)

users1 = ["Anna", "Alex", "Victor"]
users2 = users1.copy()
users2.append("Elena")
print(users1)
print(users2)

