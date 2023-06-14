# Задание:
# https://i.gyazo.com/4e5b59dea4d7a418b861391511abcf9b.png

# Решение:
def get_word_indices(strings: list[str]) -> dict:
    strings = [i.lower() for i in strings]
    li_full = [i.split() for i in strings]
    li_small = []
    for i in strings:
        li_small.extend(i.split())
    di = {}
    set_li = set(li_small)
    for i in set_li:
        new_li = []
        for j in range(len(li_full)):
            if i in li_full[j]:
                new_li.append(j)
        di.setdefault(i, new_li)
    return di

# Альтернатива (not_mine):
# def get_word_indices(strings: list[str]) -> dict:
#     d = {}
#     for i, k in enumerate(strings):
#         for j in k.lower().split():
#             d.setdefault(j, []).append(i)
#     return d