# Задание:
# https://i.gyazo.com/2fc18d57ba6465499c6637dc2e2118ff.png

# Решение:
def check_password(password):
    count_dig = 0
    count_up = False
    count_sym = False
    if len(password) >= 10:
        for i in password:
            if i.isdigit:
                count_dig += 1
            if i.isupper():
                count_up = True
            if i in ("!@#$%*"):
                count_sym = True
    if count_dig >= 3 and count_up == True and count_sym == True:
        print("Perfect password")
    else:
        print("Easy peasy")

# Альтернатива (not mine):
# def  check_password(p):
#     numbers = [i for i in p if i.isdigit()]
#     char = [i for i in p if i.isupper()]
#     symb = [i for i in p if i in  "!@#$%*"  ]
#
#     print("Pefrect password" if len(numbers) >= 3 and len(char) >= 1 and len(symb) >= 1 and len(p) >= 10 else "Easy peasy")