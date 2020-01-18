

def sequence(x, y):
    if x < y:
        return "parameter x harus lebih besar dari y"

    result = []
    A = y

    while True:
        result.append(A)
        A = A**2 % x
        x += 1
        if A in [0, 1]:
            break

    result.append(A)

    return result


print(sequence(3, 7))
print(sequence(5, 3))
print(sequence(16, 5))
