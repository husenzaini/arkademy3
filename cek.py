# i = 0
# while i < 5:
#     print(i)
#     i = i + 1
#     if i == 3:
#         continue


def sequence(x, y):
    if x < y:
        return "parameter x harus lebih besar dari y"

    result = []
    A = y

    while A not in [0, 1]:
        result.append(A)
        A = A**2 % x
        x += 1

    result.append(A)

    return result


print(sequence(3, 7))
print(sequence(5, 3))
print(sequence(16, 5))
