# Задача:
# https://i.gyazo.com/3deabfd7a15d65a7e9eb1955fa345ef5.png

# Решение:
n, m = map(int, input().split())
n_list = list(map(int, input().split()))
m_list = list(map(int, input().split()))
result = []
while n_list and m_list:
    if n_list[0] >= m_list[0]:
        result.append(m_list[0])
        m_list.pop(0)
    else:
        result.append(n_list[0])
        n_list.pop(0)
if not n_list:
    result.extend(m_list)
elif not m_list:
    result.extend(n_list)
print(*result)