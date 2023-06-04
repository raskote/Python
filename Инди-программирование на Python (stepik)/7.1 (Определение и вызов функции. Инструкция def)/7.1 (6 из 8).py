# Задание:
# https://i.gyazo.com/cb3d2cea6d2f29b5f8792136c309f942.png

# Решение:
def get_body_mass_index(weight, height):
    index = weight / ((height/100) ** 2)
    if index < 18.5:
        print("Недостаточная масса тела")
    elif 18.5 <= index <= 25:
        print("Норма")
    else:
        print("Избыточная масса тела")
    print(weight, height)
get_body_mass_index(70, 170)