# Задача:
# https://i.gyazo.com/6515cae572e490e6be5c3927ef43c071.png

# Решение:
workers = {
    'employer1': {'name': 'Jhon', 'salary': 7500},
    'employer2': {'name': 'Emma', 'salary': 8000},
    'employer3': {'name': 'Brad', 'salary': 500}
}
for person in workers:
    if workers[person]['name'] == "Brad":
        workers[person]['salary'] = 8500
print(workers)