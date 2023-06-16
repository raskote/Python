# Задание:
# https://i.gyazo.com/ffb8fa1ec99afd2563b4ea654fbff333.png

# Решение:
def create_matrix(size: int = 3, up_fill: int = 0, down_fill: int = 0):
    li = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            if i == j:
                li[i][j] = i+1
            if i < j:
                li[i][j] = up_fill
            if i > j:
                li[i][j] = down_fill
    return li

# Альтернатива (not mine):
# def create_matrix(size: int=3, up_fill: int=0, down_fill: int=0):
#     matrix = [[i]*size for i in range(1, size+1)]
#     for i in range(size):
#         for j in range(size):
#             if i > j:
#                 matrix[i][j] = down_fill
#             elif i < j:
#                 matrix[i][j] = up_fill
#     return matrix