# Задача:
# https://i.gyazo.com/7c759a6b1d6093fea259130c4c4b3788.png

# Решение:
countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()
flag = False
for key, value in countries.items():
    if city in value:
        flag = True
        print(f'INFO: {city} is a city in {key}')
if flag == False:
    print(f'ERROR: Country for {city} not found')
