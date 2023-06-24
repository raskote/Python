# Задание:
# https://i.gyazo.com/ada4927ac5f7023a4134e684fa35d84b.png

# Решение:
def get_combin(n: int, k: int):
    if k == 0 or k == n:
        return 1
    if 0 <= k <= n:
        return get_combin(n-1, k) + get_combin(n-1, k-1)

n, k = int(input()), int(input())
print(get_combin(n, k))