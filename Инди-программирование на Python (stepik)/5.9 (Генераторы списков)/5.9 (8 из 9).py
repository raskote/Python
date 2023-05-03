# Задача:
# https://i.gyazo.com/4f77831f477db4e1f90029e95779aaff.png

# Решение:
from string import ascii_uppercase
print([ascii_uppercase[i]*(i+1) for i in range(int(input()))])
