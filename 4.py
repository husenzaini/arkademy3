def picture(panjang):
    if type(panjang) != int or panjang % 2 == 0:
        print("Parameter harus angka dan ganjil!")

    print("--- " + str(panjang) + " ---")

    for i in range(panjang):
        for c in range(panjang):
            if c == panjang-1 or i == panjang//2 or c == 0:
                print("*", end=" ")
            else:
                print("=", end=" ")
        print()


picture(9)
# print(picture(3))
# print(picture('hem'))
