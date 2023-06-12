# Задание:
# https://i.gyazo.com/268e2efe7eeb09e4898668105499e326.png

# Решение:

MIN_DRIVING_AGE = 18
def allowed_driving(name: str, age: int) -> None:
    if age >= MIN_DRIVING_AGE:
        print(f"{name} может водить")
    else:
        print(f"{name} еще рано садиться за руль")

