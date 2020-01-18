def sequence(x, y):
    if x < y:
        print("parameter x harus lebih besar dari y")

    result = []
    A = y

    while A not in [0, 1]:
        result.append(A)
        A = A**2 % x
        x += 1

    result.append(A)

    print('array :' + str(result))
    print('count' + str(len(result)))


sequence(3, 7)
sequence(5, 3)
sequence(16, 5)
