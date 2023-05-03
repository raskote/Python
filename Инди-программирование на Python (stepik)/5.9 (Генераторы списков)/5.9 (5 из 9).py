# Задача:
# https://i.gyazo.com/d74d13c93d30a6c03e6dedbba4a69c69.png

# Решение:
a, b = map(int, input().split())
print([i**2 if a<=b else i**3 for i in (range(a,b+1) if a<=b else range(a,b-1,-1))])


# Альтернатива (mine):
# a, b = map(int, input().split())
# if a<=b:
#     print([i**2 for i in range(a, b+1)])
# else:
#     print([i**3 for i in range(b, a+1)][::-1])

# Альтернатива (not mine):
# a, b = map(int, input().split())
# print([i**2 for i in range(a, b + 1)] or [i**3 for i in range(a, b - 1, -1)])